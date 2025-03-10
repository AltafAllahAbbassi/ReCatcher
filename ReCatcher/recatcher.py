import os
import uuid
import pandas as pd
from collections import Counter
from scipy.stats import mannwhitneyu
from statistics import mean
from tqdm import tqdm
from ReCatcher.utils import unnecessary_conditional_block, unnecessary_else, variable_naming, sub_readable, syntax_error, missing_import_declaration, code_duplication, comment_duplication
from ReCatcher.utils import read_jsonl, extract_method_name, save_json, measure_execution_performance, execute_unittest, execute_assert_tests, write_jsonl_line
from ReCatcher.constants import BENCHMARKS
import matplotlib
matplotlib.use('Agg') 

class ReCatcher(object):
    def __init__(self, benchmark=BENCHMARKS["HUMANEVAL_PLUS"], n_rep = 5, large_timeout=600, test_timeout=120):
        self.n_rep = n_rep # how many times we repeat the execution for perforamnce
        self.large_timeout = large_timeout
        self.test_timeout = test_timeout
        # self.method_call =  ## for large inputs
        if BENCHMARKS["HUMANEVAL_PLUS"] in benchmark:
            self.benchmark = read_jsonl(benchmark)
            self.benchmark_name = "humaneval"
            
        if BENCHMARKS["BIGCODEBENCH"] in benchmark:
            benchmark_df = pd.read_parquet(benchmark)
            self.benchmark = benchmark_df.to_dict(orient="records")
            self.benchmark_name = "bigcodebench"

    def test_regression(self, result1_df, result2_df, method, result_dir, large_input=True, timeout=True):
        os.makedirs(result_dir, exist_ok=True)
        ## static  properties
        if method in [unnecessary_conditional_block, unnecessary_else, variable_naming, sub_readable, syntax_error, syntax_error, missing_import_declaration, code_duplication, comment_duplication]:
            result_file1, summary1 = self.test_static(result1_df, method=method, result_dir=result_dir)
            result_file2, summary2 = self.test_static(result2_df, method=method, result_dir=result_dir)
            print(f"Results1 saved in: {result_file1}")
            print(f"Results2 saved in: {result_file2}")
            if len(summary1.keys()) == len(summary2.keys()):
                x1 = [summary1[key]["Total raised"] for key in summary1.keys()]
                x2 = [summary2[key]["Total raised"] for key in summary2.keys()]
            
        ## general logic
        elif method == "general_logic":
            result_file1, summary1 = self.test_general_logic(result_df=result1_df, result_dir=result_dir)
            result_file2, summary2 = self.test_general_logic(result_df=result2_df, result_dir=result_dir)
            print(f"Results1 saved in: {result_file1}")
            print(f"Results2 saved in: {result_file2}")
            if len(summary1.keys()) == len(summary2.keys()):
                x1 = [summary1[key]["Correct code"] for key in summary1.keys()]
                x2 = [summary2[key]["Correct code"] for key in summary2.keys()]

        ## performance
        elif method == "performance":
            result_file, results = self.test_performance(result1_df, result2_df, result_dir, large_input, timeout)
            print(f"Results saved in: {result_file}")            
            return results, results
        
        
        if method == "general_logic" or method in [unnecessary_conditional_block, unnecessary_else, variable_naming, sub_readable, syntax_error, syntax_error, missing_import_declaration, code_duplication, comment_duplication]:
            mean1= mean(x1)
            mean2 = mean(x2)
            print(f"Mean1: {mean1}")
            print(f"Mean2: {mean2}")
            u, p_value = mannwhitneyu(x1, x2, alternative='two-sided')
            effect_ = u/(len(x1)*len(x2))
            if p_value<0.05:
                    print("There is a significant difference")
            else:
                    print("There is no difference")
            print(f"p-value: {p_value}")
            print(f"u: {u}")
            print(f"effect_size: {effect_}")
            return summary1, summary2
        
        if method == "measure_performance":
            x1, x2 = self.measure_performance(result_df=result1_df, result_dir=result_dir)
            print(x1, x2)
            
            x1, x2 = self.measure_performance(result_df=result2_df, result_dir=result_dir)
            print(x1, x2)
        
    def test_static(self, result_df,  method, result_dir):
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}_{method}.json")
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in range(n_rep):
            result = []
            for i in tqdm(range(len(result_df))):
            # for i in tqdm(range(len(result_df))):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "inef_test": method(code), 
                    # "correct_code": correct_code
                    
                }
                write_jsonl_line(result_file, to_save)
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Total raised": len([x for x in result if x["inef_test"]]),
                                # "Correct code raised": len([x for x in result if x["inef_test"] and x["correct_code"]]),
                                # "Incorrect code raised": len([x for x in result if x["inef_test"] and not x["correct_code"]]),
                                }
        return summary, result_file
    
    def test_general_logic(self, result_df, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_general_logic_humaneval(result_df, result_dir)
        if self.benchmark_name == "bigcodebench":
            return self.test_general_logic_bigcode_bench(result_df, result_dir)

    def test_general_logic_humaneval(self, result_df, result_dir):
        os.makedirs(result_dir, exist_ok=True)
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.jsonl")
        summary = {}
        results = {}
        for j in tqdm(range(n_rep)):
            result = []
            for i in tqdm(range(len(result_df))):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                method_name = extract_method_name(code)[0]
                test = code + "\n"+ self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                to_save = {
                    "exp": f"exp_{j}",
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "test": test
                }
                try:
                    exec(test)
                    to_save["correct_code"] = True
                except:
                    to_save["correct_code"] = False
                write_jsonl_line(result_file, to_save)
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Correct code": len([x for x in result if not x["correct_code"]])}       
        return result_file, summary
    
    def test_general_logic_bigcode_bench(self, result_df, result_dir):
        os.makedirs(result_dir, exist_ok=True)
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.jsonl")
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in range(n_rep):
            result = []
            # for i in tqdm(range(len(result_df))):
            for i in tqdm(range(5)):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                test = code + "\n"+ self.benchmark[i]["test"] + f'\nimport io\noutput = io.StringIO()  # Create a StringIO buffer to capture the output\nloader = unittest.TestLoader()\nsuite = loader.loadTestsFromTestCase(TestCases)\nrunner = unittest.TextTestRunner(verbosity=2, stream=output)  # Direct output to the buffer\nrunner.run(suite)\ntest_output = output.getvalue()  # Get the captured output'
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "test": test, 
                    "exp": f"exp_{j}"
                }
                try:
                    to_save["correct_code"] = execute_unittest(test)
                except:
                    to_save["correct_code"] = False
                write_jsonl_line(result_file, to_save)
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Correct code": len([x for x in result if not x["correct_code"]])}
            
        return result_file, summary
        
    def test_performance(self, result1_df, result2_df, result_dir, large_input, timeout):
        # if I Have number 1, this means code 1 is worse
        assert len(result1_df) == len(self.benchmark) == len(result2_df)
        n_rep = len([x for x in result1_df.columns if x.startswith("exp")])
        time_result = []
        memory_result = []
        results = []
        summary = {}
        for i in tqdm(range(len(result1_df))):
        # for i in tqdm(range(20)):
            task_id = result1_df["task_id"][i]
            prompt = result1_df["prompt"][i]
            mem1 = []
            mem2 = []
            time1 = []
            time2 = []
            for j in range(n_rep):
                # forming unit test of human eval 
                code1 = result1_df[f"exp_{str(j)}"][i]
                code2 = result2_df[f"exp_{str(j)}"][i]
                
                if large_input and timeout:
                    timeout_ = self.large_timeout
                elif not large_input and timeout:
                    timeout_ = self.test_timeout
                elif not timeout:
                    timeout_ = 0
                    
                
                if self.benchmark_name == "humaneval" and not large_input:
                    method_name = extract_method_name(code1)[0]
                    test1 = code1 + "\n" + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                    test2 = code2 + "\n" +self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                    method = execute_assert_tests
                if self.benchmark_name == "humaneval" and large_input:
                    test1 = code1 + self.method_call[i]["method_call"]
                elif self.benchmark_name == "bigcodebench":
                    test1 =code1 + "\n"+ self.benchmark[i]["test"] + f'\nimport io\noutput = io.StringIO()  # Create a StringIO buffer to capture the output\nloader = unittest.TestLoader()\nsuite = loader.loadTestsFromTestCase(TestCases)\nrunner = unittest.TextTestRunner(verbosity=2, stream=output)  # Direct output to the buffer\nrunner.run(suite)\ntest_output = output.getvalue()  # Get the captured output'
                    test2 =code2 + "\n"+ self.benchmark[i]["test"] + f'\nimport io\noutput = io.StringIO()  # Create a StringIO buffer to capture the output\nloader = unittest.TestLoader()\nsuite = loader.loadTestsFromTestCase(TestCases)\nrunner = unittest.TextTestRunner(verbosity=2, stream=output)  # Direct output to the buffer\nrunner.run(suite)\ntest_output = output.getvalue()  # Get the captured output'
                    method = execute_unittest
                # else:
                #     exit()
                try:
                    
                    per1 = measure_execution_performance(code=test1, method=method, n_repetition=self.n_rep, timeout=timeout_)
                    per2 = measure_execution_performance(code=test2, method = method, n_repetition=self.n_rep, timeout=timeout_)
                    if not(per1["execution_time"] =="FAIL" or per2["execution_time"] =="FAIL" or per1["memory_usage"] =="FAIL" or per1["memory_usage"] =="FAIL"):
                        time1.extend(per1["execution_time"])
                        time2.extend(per2["execution_time"])
                        mem1.extend(per1["memory_usage"])
                        mem2.extend(per2["memory_usage"])

                except:
                    pass
            if len(time1) and len(time2) and len(mem1) and len(mem2):           
                _, time_p_value = mannwhitneyu(time1, time2, alternative='two-sided')
                _, mem_p_value = mannwhitneyu(mem1, mem2, alternative='two-sided')            
                if time_p_value<0.05:
                    if mean(time1)>mean(time2):
                        time = 1
                    else:
                        time = 2
                else:
                    time = 0
                            
                if mem_p_value<0.05:
                    if mean(mem1)>mean(mem2):
                        memory = 1
                    else:
                        memory = 2
                else:
                    memory=0
                time_result.append(time)
                memory_result.append(memory)
                if i %10 == 0 and i>0:
                    print(f"################ {i} ################")
                    print(f"Memory: {dict(Counter(memory_result))}")
                    print(f"Time: {dict(Counter(time_result))}")
                            
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "mem_result": memory, 
                    "time_reuslt": time
                    }
                results.append(to_save)
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
        summary["time"] = dict(Counter(time_result))
        summary["memory"] = dict(Counter(memory_result))
        return  result_file, summary
    
    def measure_performance(self, result_df, result_dir):
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        avg_times = []
        avg_memories = []
        for i in tqdm(range(20)):
        # for i in tqdm(range(len(result_df))):
            task_id = result_df["task_id"][i]
            prompt = result_df["prompt"][i]
            memory = []
            time = []
            for j in range(n_rep):
                # forming unit test of human eval 
                code = result_df[f"exp_{str(j)}"][i]
                
                if self.benchmark_name == "humaneval":
                    method_name = extract_method_name(code)[0]
                    test = code + "\n" + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                    method = execute_assert_tests

                elif self.benchmark_name == "bigcodebench":
                    test =code + "\n"+ self.benchmark[i]["test"] + f'\nimport io\noutput = io.StringIO()  # Create a StringIO buffer to capture the output\nloader = unittest.TestLoader()\nsuite = loader.loadTestsFromTestCase(TestCases)\nrunner = unittest.TextTestRunner(verbosity=2, stream=output)  # Direct output to the buffer\nrunner.run(suite)\ntest_output = output.getvalue()  # Get the captured output'
                    method = execute_unittest
                    performance = measure_execution_performance(code=test, method=method, n_repetition=self.n_rep, timeout=self.test_timeout)
                    if not(performance["execution_time"] =="FAIL"  or performance["memory_usage"] =="FAIL"):
                        time.extend(performance["execution_time"])
                        memory.extend(performance["memory_usage"])
            if len(time) and len(memory):
                avg_mem = mean(memory)
                avg_time = mean(time)
                avg_memories.append(avg_mem)
                avg_times.append(avg_time)
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "memory": memory, 
                    "time": time, 
                    "avg_mem" : avg_mem, 
                    "avg_time": avg_time
                    }
                write_jsonl_line(result_file, to_save)
        return result_file, {"avg_time": mean(avg_times), "avg_mem": mean(avg_memories)}


if __name__ == "__main__":
    re_catcher = ReCatcher(benchmark="", test_timeout=100)
    model = pd.read_csv("") # generated code saved path
    result_dir = ""
    print("################# SYNTAX ERROR #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=syntax_error, result_dir=result_dir)
    print(x1, x2)
    
    print("################# DECLRATION ERROR #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=missing_import_declaration, result_dir=result_dir)
    print(x1, x2)

    
    print("################# UNNECESSARY ELSE  #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=unnecessary_else, result_dir=result_dir)
    print(x1, x2)   
    
    
    print("################# UNNECESSARY CONDITIONAL BLOCK  #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=unnecessary_conditional_block, result_dir=result_dir)
    print(x1, x2) 
    
    print("################# VARIABLE NAMING  #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=variable_naming, result_dir=result_dir)
    print(x1, x2) 
    
    print("################# SUB-READALE CODE  #################") 
    x1, x2 = re_catcher.test_static(result_df=model, method=sub_readable, result_dir=result_dir)
    print(x1, x2)     