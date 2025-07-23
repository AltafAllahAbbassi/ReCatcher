import csv
import gc
import io
import multiprocessing
import os
import platform
import statistics
import subprocess
import sys
import time
import tracemalloc
import unittest

import constants

memory_limit = 2 * 1024 * 1024 * 1024  # for example: 2GB

if platform.system() != 'Windows':
    import resource
    try:
        resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
    except ValueError as e:
        print(f"Could not set memory limit: {e}", file=sys.stderr)
else:
    print("Warning: memory limiting via `resource` is not supported on Windows.", file=sys.stderr)

def run_test(test_code, q):
    result = {}
    try:
        exec(test_code, result)
        test_case_class = result.get("TestCases")
        if test_case_class:
            output = io.StringIO()
            loader = unittest.TestLoader()
            suite = loader.loadTestsFromTestCase(test_case_class)
            runner = unittest.TextTestRunner(verbosity=2, stream=output)
            runner.run(suite)
            q.put(output.getvalue())
        else:
            q.put("Error: TestCases class not defined in the code")
    except Exception as e:
        q.put(str(e))

def execute_unittest(test_code, timeout=60, memory_limit=10 * 1024 * 1024 * 1024):
    try:
        q = multiprocessing.Queue()
        test_process = multiprocessing.Process(target=run_test, args=(test_code, q))
        test_process.start()

        start_time = time.time()
        while test_process.is_alive():
            if time.time() - start_time > timeout:
                test_process.terminate()
                print("timeout")
                test_process.join()
                return False
            time.sleep(0.1)

        if not q.empty():
            test_output = q.get()
        else:
            test_output = "Error: No output captured"

        if "FAILED" in test_output:
            return False
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        gc.collect()

def measure_execution_performance(code, n_repetition=1, timeout=120):
    tracemalloc.start()
    execution_time = []
    memory_used = []
    for _ in range(n_repetition):
        gc.collect()
        start_time = time.perf_counter()
        mem_before = tracemalloc.get_traced_memory()[0] / 10 ** 6  # in MB

        pass_ = execute_unittest(code, timeout=timeout)

        # Track memory usage after execution
        mem_after = tracemalloc.get_traced_memory()[0] / 10 ** 6  # in MB

        # Track execution end time
        end_time = time.perf_counter()

        # Calculate execution time
        execution_time.append(end_time - start_time)
        memory_used.append(mem_after - mem_before)  # Memory usage difference
        if not pass_:
            return {
                "execution_time": "FAIL",
                "memory_usage": "FAIL"
            }

    return {
        "execution_time": execution_time,
        "memory_usage": memory_used
    }

import json

def filter_by_exp_and_index_by_task_id(json_path, target_exp="exp_0"):
    result = {}
    with open(json_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            try:
                entry = json.loads(line)
                #if entry.get("exp") == target_exp and "task_id" in entry and "test" in entry:
                if entry.get("exp") == target_exp and "task_id" in entry and "test" in entry and "correct_code" in entry and entry["correct_code"] == True:
                    result[entry["task_id"]] = entry["test"]
            except json.JSONDecodeError as e:
                print(f"Skipping line due to JSON error: {e}")
    return result

def save_output_comments(exp_id, task_id, code_base, code_variant, base_mean_time, variant_mean_time,
                                             evaluation_time, base_mean_memory, variant_mean_memory,
                                             evaluation_memory):
    filename = constants.REPORT_PERFORMANCE + task_id.split("/")[0] + ".csv"
    output_csv_path = os.path.join(constants.REPORT_DIRECTORY, filename)
    try:

        headers = [
            "exp_id",
            "task_id",
            "code_base",
            "code_variant",
            "mean_base_time",
            "mean_variant_time",
            "evaluation_time",
            "mean_base_memory",
            "mean_variant_memory",
            "evaluation_memory",
        ]

        if not os.path.exists(output_csv_path):
            with open(
                output_csv_path, mode="w", newline="", encoding="utf-8"
            ) as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=headers)
                writer.writeheader()
            csv_file.close()

        with open(
            output_csv_path, mode="a+", newline="", encoding="utf-8"
        ) as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            writer.writerow(
                {
                    "exp_id":exp_id,
                    "task_id" : task_id,
                    "code_base" : code_base,
                    "code_variant" : code_variant,
                    "mean_base_time" : base_mean_time,
                    "mean_variant_time" : variant_mean_time,
                    "evaluation_time" : evaluation_time,
                    "mean_base_memory" : base_mean_memory,
                    "mean_variant_memory" : variant_mean_memory,
                    "evaluation_memory" : evaluation_memory,
                }
            )

        print(f"CSV file has been successfully written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_evaluation(base_mean, variant_mean):
    if base_mean > variant_mean:
        evaluation = "CODE_BASE"
    elif base_mean < variant_mean:
        evaluation = "CODE_VARIANT"
    elif base_mean == variant_mean:
        evaluation = "EQUAL"
    else:
        evaluation = "NULL"

    return evaluation

if __name__ == "__main__":
    exps = ["exp_0", "exp_1", "exp_2", "exp_3", "exp_4", "exp_5", "exp_6", "exp_7", "exp_8", "exp_9", "exp_10"]
    try:
        for par_files in constants.INPUT_FILES_PERFORMANCE_EVALUATION:
            for one_exp in exps:

                base = filter_by_exp_and_index_by_task_id(par_files[0], one_exp)
                variant = filter_by_exp_and_index_by_task_id(par_files[1], one_exp)
                method = execute_unittest

                for task_id_base, test_base in base.items():
                    if variant.get(task_id_base) is not None:
                        code_base = base.get(task_id_base)
                        base_results = measure_execution_performance(code_base, 5)
                        code_variant = variant.get(task_id_base)
                        variant_results = measure_execution_performance(code_variant, 5)
                        base_mean_time = statistics.mean(base_results.get("execution_time"))
                        variant_mean_time = statistics.mean(variant_results.get("execution_time"))
                        base_mean_memory = statistics.mean(base_results.get("memory_usage"))
                        variant_mean_memory = statistics.mean(variant_results.get("memory_usage"))

                        evaluation_time = get_evaluation(base_mean_time, variant_mean_time)
                        evaluation_memory = get_evaluation(base_mean_memory, variant_mean_memory)

                        save_output_comments(one_exp, task_id_base, code_base, code_variant, base_mean_time, variant_mean_time,
                                             evaluation_time, base_mean_memory, variant_mean_memory,
                                             evaluation_memory)

    except subprocess.CalledProcessError as e:
        print(f"Failed to install required packages: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
