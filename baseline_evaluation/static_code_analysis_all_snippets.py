import csv
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import uuid
from collections import defaultdict

import constants

REQUIRED_PACKAGES = [
    "flake8",
    "flake8-return",
    "flake8-cognitive-complexity",
    "flake8-bugbear"
    "ruff"
]

VIOLATION_RULES = [
    "cc_total",
    "mi",
]

def run_pylint_similarity(code: str, min_lines: int = 4) -> str:
    code = textwrap.dedent(code)

    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [
                sys.executable, "-m", "pylint",
                "--disable=all",
                "--enable=similarities",
                f"--min-similarity-lines={min_lines}",
                "--verbose",
                tmp_path
            ],
            capture_output=True,
            text=True
        )
        print("====== RAW OUTPUT ======")
        print(result.stdout)
        return result.stdout
    finally:
        os.remove(tmp_path)


from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze as raw_analyze
import textwrap

def compute_complexity_metrics(code: str) -> dict:
    import warnings
    metrics = {
        "cc_total": 0,
        "mi": 0,
    }

    try:
        code = textwrap.dedent(code)

        # Raw metrics
        raw = raw_analyze(code)
        metrics["mi"] = mi_visit(code, False)

        functions = cc_visit(code)
        metrics["cc_total"] = sum(f.complexity for f in functions)

    except Exception as e:
        warnings.warn(f"[WARN] Complexity analysis failed: {e}")

    return metrics

def install_missing_packages():
    for package in REQUIRED_PACKAGES:
        module_name = package.split("-")[0]
        if importlib.util.find_spec(module_name) is None:
            print(f"Installing missing package: {package}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def write_temp_files(code_list, temp_dir):
    temp_files = {}
    for i, code in enumerate(code_list):
        filename = f"snippet_{i}_{uuid.uuid4().hex[:6]}.py"
        full_path = os.path.join(temp_dir, filename)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(code)
        temp_files[full_path] = filename
    return temp_files

def run_flake8_on_files(file_paths):
    cmd = [sys.executable, "-m", "flake8", "--exit-zero", *file_paths]
    result = subprocess.run(cmd, capture_output=True, text=True)
    combined_output = result.stdout + "\n" + result.stderr
    return combined_output

def parse_flake8_output(output):
    violations = defaultdict(int)
    for line in output.strip().split('\n'):
        if not line.strip() or ':' not in line:
            continue
        parts = line.split(":", 4)
        if len(parts) < 4:
            continue
        message = parts[4].strip()
        rule = message.split()[0]
        if rule in VIOLATION_RULES:
            violations[rule] += 1
    return dict(violations)

def write_header(file_path):
    if not os.path.exists("results/static/"+file_path):
        with open("results/static/"+file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["snippet_id"] + VIOLATION_RULES)

def append_row(file_path, snippet_id, violations):
    row = [snippet_id]
    for rule in VIOLATION_RULES:
        row.append(violations.get(rule, 0))
    with open("results/static/"+file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)

def get_correct_code(model):
    temp_dict = {}
    for json_str in model:
        result = json.loads(json_str)
        base_exp_id = result['exp']
        task_id = result['task_id']

        if base_exp_id not in temp_dict:
            temp_dict[base_exp_id] = {task_id: result['test']}
        else:
            if task_id not in temp_dict[base_exp_id]:
                temp_dict[base_exp_id][task_id] = result['test']

    return temp_dict

def get_static_analysis(input_file, exp_id, task_id, code_snippet, temp_dir):
    filename = os.path.basename(input_file).removesuffix('.jsonl')  # Requires Python 3.9+
    model_name = os.path.basename(os.path.dirname(input_file))
    benchmark_name = os.path.basename(os.path.dirname(os.path.dirname(input_file)))

    output_file_name = "ALL_static_analysis_" + benchmark_name + "_" + model_name + "_" + input_file.rsplit('/', 1)[
        -1].removesuffix('.jsonl') + ".csv"
    write_header(output_file_name)

    code = code_snippet

    snippet_id = exp_id + "_" + task_id

    if code is not None:
        temp_file_map = write_temp_files([code], temp_dir)
        file_path = list(temp_file_map.keys())[0]

        metrics = compute_complexity_metrics(code)

        append_row(output_file_name, snippet_id, metrics)

        print(f"Processed snippet {snippet_id}")

if __name__ == "__main__":
    try:
        install_missing_packages()

        with tempfile.TemporaryDirectory() as temp_dir:
            for par_file in constants.INPUT_FILES_LOGIC_EVALUATION:

                    with open(par_file, 'r') as json_file:
                        base_model = get_correct_code(list(json_file))

                    for exp_id_base, base_tasks in base_model.items():
                            for base_task in base_tasks:
                                get_static_analysis(par_file, exp_id_base, base_task, base_tasks.get(base_task), temp_dir)

    except subprocess.CalledProcessError as e:
        print(f"Failed to install required packages: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")