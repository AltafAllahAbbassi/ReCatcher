# ReCatcher Replication Package

This repository contains the replication package for **ReCatcher: Towards Regression Testing for LLMs in Code Generation**.

## Repository Structure

- `code_generation/` - Contains scripts to generate code snippets using LLMs.
- `ReCatcher/` - The implementation of the ReCatcher framework.
- `Examples/` - Provides an example demonstrating how to use ReCatcher.

## Data Availability

Our data is publicly available at:
- **Generated code snippets**: [Zenodo link]
- **Regression testing results**: [Zenodo link]

## Setup Instructions

### 1. Create and Activate a Virtual Environment
```bash
conda create --name ReCatcher python=3.9
conda activate ReCatcher
```
### 2. Install Dependencies

```bash
pip install -e .
pip install -r requirements.txt
pip install -r bigcodebench_requirements.txt` 
```
### 3. Install and Configure PMD

#### Install PMD

Follow the official installation guide: [PMD Documentation](https://pmd.github.io/pmd/pmd_userdocs_cpd)

#### Add PMD to System Path

For Linux:
```bash
`export PATH=$PATH:/path/to/pmd-dist-7.8.0-bin/pmd-bin-7.8.0/bin` 
```
### 4. Configure Pylint for Custom Checker

To integrate ReCatcher's custom Pylint checker for detecting **Unnecessary Conditional Blocks**, copy the file:

```bash 
cp custom_checkers/custom_checker.py envs/ReCatcher/lib/python3.9/site-packages/pylint/checkers/` 
```

ReCatcher is now set up and ready to run.

----------