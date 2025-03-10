import os
import json
import tempfile
from io import StringIO
from pylint import lint
import re
from pylint.reporters.json_reporter import JSONReporter
import time
import tracemalloc
import gc
import difflib
import subprocess
import multiprocessing
import unittest
import io
import gc
import time
import threading
import resource
from ReCatcher.constants import CODE_DUPLICATION_MIN_COUNT, PMD_COMMAND_TEMPLATE, COMMENT_DUPLICATION_THRESHOLD, COMMENT_DUPLICATION_MIN_COUNT


def get_pylint_output(code):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(code.encode('utf-8'))
        temp_filename = temp_file.name
    
    output = StringIO()
    reporter = JSONReporter(output)
    
    try:
        pylint_opts = [temp_filename, '--disable=C0114,C0304', '--load-plugins=custom_checkers/custom_checker.py']
        lint.Run(pylint_opts, reporter=reporter)
    except SystemExit as e:
        if e.code != 0:
            pass
    
    pylint_output = json.loads(output.getvalue())
    return pylint_output

def unnecessary_else(code):
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        if output["message-id"] in  ["R1705", "W0107", "R1720", "R1723"]:
            return True
    return False

def unnecessary_conditional_block(code):
    pattern = (
        r"if\s*\(?.+\)?\s*:\s*\n"  # Match `if` statement with optional parentheses
        r"\s*return\s+True\s*\n"   # Match `return True`
        r"\s*return\s+False"       # Match `return False` directly after the `if` block
    )
    match = re.search(pattern, code, re.DOTALL)
    if bool(match):
        return True
    
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        if output["message-id"] in  ["R1710"]:
            return True
    return False

def missing_import_declaration(code):
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        # undefined-variable / E0602
        # undefined-loop-variable / W0631
        if (output["message-id"] == "E0602") or (output["message-id"] == "W0631"):
            return True
    return False

def syntax_error(code):
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        if output["message-id"] == "E0001":
            return True
    return False

def variable_naming(code):
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        # invalid-name / C0103 when the naming do not conform 
        # redefined-builtin / W0622 for example when 
        # redefined-outer-name / W0621 for variable shadowing 
        # redefined-loop-name / W2901 shadowing inside names 
        # disallowed-name / C0104 variable naming that are not allowed 
        if output["message-id"] in ["C0103", "C0104", "W2901", "W0621", "W0622"]:
            return True
    return False

def code_duplication(code, min_token=CODE_DUPLICATION_MIN_COUNT):
    temp_file_path = None
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix=".py") as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name
            formatted_command = PMD_COMMAND_TEMPLATE.format(min_token, temp_file_path)
    result = subprocess.run(
                formatted_command,
                shell=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
    if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)
    return bool(result.stdout.strip())

def comment_duplication(code, threshold=COMMENT_DUPLICATION_THRESHOLD, min_count=COMMENT_DUPLICATION_MIN_COUNT):
    lines = code.splitlines()
    comments = []
    duplicates = {}

    # Extract comments from the code
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("#"):
            comments.append(stripped_line)
                
    if not comments:
        return False
    # Check for similar comments
    for i in range(len(comments)):
        for j in range(i + 1, len(comments)):
            # Calculate similarity ratio
            similarity = difflib.SequenceMatcher(None, comments[i], comments[j]).ratio()
            if similarity >= threshold:
                # Count similar comments
                duplicates[comments[i]] = duplicates.get(comments[i], 0) + 1
                duplicates[comments[j]] = duplicates.get(comments[j], 0) + 1
                if duplicates[comments[i]] >= min_count or duplicates[comments[j]] >= min_count:
                    return True

    return False

def sub_readable(code):
    """
    At this stage we did not consider this list, but in future it may include
    • consider-iterating-dictionary / C0201
    • consider-using-any-or-all / C0501
    • consider-using-dict-items / C0206
    • consider-using-enumerate / C0200
    • consider-using-f-string / C0209
    • consider-alternative-union-syntax / R6003
    • consider-merging-isinstance / R1701
    • consider-refactoring-into-while-condition / R3501
    • consider-swap-variables / R1712
    • consider-using-alias / R6002
    • consider-using-assignment-expr / R6103
    • consider-using-augmented-assign / R6104
    • consider-using-dict-comprehension / R1717
    • consider-using-from-import / R0402
    • consider-using-generator / R1728
    • consider-using-get / R1715
    • consider-using-in / R1714
    • consider-using-join / R1713
    • consider-using-max-builtin / R1731
    • consider-using-min-builtin / R1730
    • consider-using-namedtuple-or-dataclass / R6101
    • consider-using-set-comprehension / R1718
    • consider-using-sys-exit / R1722
    • consider-using-ternary / R1706
    • consider-using-tuple / R6102
    • consider-using-with / R1732
    • consider-ternary-expression / W0160
    • unnecessary-lambda / W0108
    • unnecessary-lambda-assignment / C3001
    • unnecessary-direct-lambda-call / C3002
    • unidiomatic-typecheck / C0123
    """
    pylint_output = get_pylint_output(code)
    for output in pylint_output:
        # for now we included : type and isinstance/ unecessary lambda assignmnet, unnecessary lambda, unecessary lambda with reduce
        if output["message-id"] in  ["C0123", "C3001", "W0108", "W9999"]:
            return True
    return False
    
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as json_file:
        for line in json_file:
            data.append(json.loads(line))
    return data

def extract_method_name(code):
    # Regular expression to match 'def method_name('
    pattern = r"def\s+(\w+)\s*\("
    # Find all matches
    method_names = re.findall(pattern, code)
    return method_names

def save_json(save_file, object):
    with open(save_file, 'w') as json_file:
        json.dump(object, json_file, indent=4)

def measure_execution_performance(code, n_repetition, method, timeout):        
            tracemalloc.start()
            execution_time = []
            memory_used = []
            for _ in range(n_repetition):
                gc.collect()
                start_time = time.perf_counter()
                mem_before = tracemalloc.get_traced_memory()[0] / 10**6  # in MB

                pass_ = method(code, timeout=timeout)

                # Track memory usage after execution
                mem_after = tracemalloc.get_traced_memory()[0] / 10**6  # in MB

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
    
    
def execute_assert_tests(test_code, timeout):
    ## if no timeout is defined
    if timeout == 0:
        try:
            exec(test_code)
            return True
        except:
            return False
        
    def execute_code(code, queue):
        try:
            exec(code, {})
            queue.put(True)
        except:
            queue.put(False)
            
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=execute_code, args=(test_code, queue))
    process.start()
    process.join(timeout=timeout)
    if process.is_alive():
        process.terminate()
        process.join()
        print("Timeout")
        return False
    return queue.get() if not queue.empty() else False



def execute_unittest(test_code, timeout=60, memory_limit=10*1024*1024*1024):
    try:
        result = {}
        def run_test(q):
            try:
                resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
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
        q = multiprocessing.Queue()
        
        # Create a process to run the test
        test_process = multiprocessing.Process(target=run_test, args=(q,))
        test_process.start()
        # Monitor the process and enforce the timeout
        start_time = time.time()
        while test_process.is_alive():
            if time.time() - start_time > timeout:
                test_process.terminate()  # Force termination after timeout
                print("timeout")
                test_process.join()  # Ensure process termination is complete
                return False
            time.sleep(0.1)  # Avoid tight looping
        # Get the captured test output from the queue        # print(test_output)

        if not q.empty():
            test_output = q.get()
        else:
            test_output = "Error: No output captured"
        # Check for failures or errors in the output
        # print(test_output)
        if "FAILED" in test_output:
            return False
        return True
    except Exception as e:
        return False
    finally:
        gc.collect()
        
        
def write_jsonl_line(file_, line):
    with open(file_, "a", encoding="utf-8") as file:
        json.dump(line, file)
        file.write("\n") 