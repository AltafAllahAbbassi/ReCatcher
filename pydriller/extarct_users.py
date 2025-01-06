import os
import re
import requests
import subprocess
import shutil
from pydriller import Repository
from validate_email import validate_email
from constants import keywords, languages, HEADERS, results_per_page, max_pages

def extract_emails(repositories):
    emails = set()
    for repo_url in repositories:
        print(f"Analyzing repository: {repo_url}")
        # Create a temporary directory for cloning
        repo_name = repo_url.split("/")[-1].replace(".git", "")
        temp_dir = f"./temp_{repo_name}"
        
        # Clone repository locally if not already done
        if not os.path.exists(temp_dir):
            try:
                subprocess.run(["git", "clone", repo_url, temp_dir], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Failed to clone repository {repo_url}: {e}")
                continue
        
        # Use PyDriller to extract email addresses
        try:
            for commit in Repository(temp_dir).traverse_commits():
                if commit.author.email:
                    emails.add(commit.author.email)
        except Exception as e:
            print(f"Error processing repository {repo_url}: {e}")
        finally:
            # Clean up the cloned repository
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    return emails

def search_github(keyword, language):
    repositories = set()  # Use a set to avoid duplicate repositories
    for page in range(1, max_pages + 1):
        query = f"{keyword} language:{language}"
        params = {
            "q": query,
            "per_page": results_per_page,
            "page": page,
        }
        print(f"Searching for '{query}' (Page {page})...")
        response = requests.get(SEARCH_URL, headers=HEADERS, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
            break

        data = response.json()
        for item in data.get("items", []):
            # Extract repository URL
            repo_url = item["repository"]["html_url"]
            repositories.add(repo_url)

        # Stop if there are no more results
        if "incomplete_results" in data and not data["incomplete_results"]:
            break
    return repositories

def is_internal_host(email):
    domain = email.split('@')[-1]
    # Regex to detect hostnames or IP-like structures
    return re.match(r'^[a-zA-Z0-9.-]*(\d{1,3}\.){3}\d{1,3}.*$', domain) is not None

def is_internal_domain(email):
    internal_tlds = ['.local', '.internal', '.localdomain']
    domain = email.split('@')[-1]
    return any(domain.endswith(tld) for tld in internal_tlds)

def is_complex_internal_domain(email):
    domain = email.split('@')[-1]
    # Match long subdomains or specific organizational patterns
    return len(domain.split('.')) > 3 or re.search(r'[0-9a-fA-F-]{36}', domain) is not None

def is_email(email):
    ## no reply 
    pattern = r".*noreply.*"
    if re.match(pattern, email):
        return False
    
    ## emails that are all numbers eg 165489743489@ 
    pattern = r"^[0-9]*@"
    if re.match(pattern, email):
        return False
    
    if email in ['.local', '.broadband', 'instance', 'internal', "root@", ".lan", 'admin@', '.home', 'isl-', 'SUNet', 'ubuntu']:
        return False
    return validate_email(email)


if __name__ == "__main__":    
    all_repositories = set()
    for keyword in keywords:
        for language in languages:
            repos = search_github(keyword, language)
            all_repositories.update(repos)

    all_emails = extract_emails(repositories=all_repositories)
    emails = [email for email in all_emails if is_email(email)]
    
    with open("collected_repositories.txt", "w") as file:
        for repo in sorted(all_repositories):
            file.write(repo + "\n")
    
    with open("collected_emails.txt", "w") as file:
        for email in sorted(emails):
            file.write(email + "\n")
            