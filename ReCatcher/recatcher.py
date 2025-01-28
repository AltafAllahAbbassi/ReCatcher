import os
import uuid
import pandas as pd
from collections import Counter
from scipy.stats import mannwhitneyu
from statistics import mean
from tqdm import tqdm
from ReCatcher.utils import unnecessary_conditional_block, unnecessary_else, variable_naming, sub_readable, syntax_error, missing_import_declaration, code_duplication, comment_duplication
from ReCatcher.utils import read_jsonl, extract_method_name, save_json, measure_execution_performance, execute_unittest, execute_assert_tests
from ReCatcher.constants import BENCHMARKS
import matplotlib
matplotlib.use('Agg') 
from difflib import SequenceMatcher

class ReCatcher(object):
    def __init__(self, benchmark=BENCHMARKS["HUMANEVAL_PLUS"], n_rep = 5, large_timeout=180, test_timeout=45):
        self.n_rep = n_rep # how many times we repeat the execution for perforamnce
        self.large_timeout = large_timeout
        self.test_timeout = test_timeout
        if BENCHMARKS["HUMANEVAL_PLUS"] in benchmark:
            self.benchmark = read_jsonl(benchmark)
            self.benchmark_name = "humaneval"
            self.method_call = read_jsonl("/workspace/ReCatcher/data/humaneval_plus/humaneval_method_call.jsonl")
 
            
        if BENCHMARKS["BIGCODEBENCH"] in benchmark:
            benchmark_df = pd.read_parquet(benchmark)
            self.benchmark = benchmark_df.to_dict(orient="records")
            self.benchmark_name = "bigcodebench"
            # self.method_call 
            # self.large_timeout = 
            # self.test_timeout = 120

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
                mean1= mean(x1)
                x2 = [summary2[key]["Total raised"] for key in summary2.keys()]
                mean2 = mean(x2)
                print(f"Mean1: {mean1}")
                print(f"Mean2: {mean2}")
                _, p_value = mannwhitneyu(x1, x2, alternative='two-sided')
                if p_value<0.05:
                    print("There is a significant difference")
                else:
                    print("There is no difference")
            else:
                print("The number of experiments is different. We can't perform test")
            return summary1, summary2
            
        ## general logic
        elif method == "general_logic":
            result_file1, summary1 = self.test_general_logic(result_df=result1_df, result_dir=result_dir)
            result_file2, summary2 = self.test_general_logic(result_df=result2_df, result_dir=result_dir)
            print(f"Results1 saved in: {result_file1}")
            print(f"Results2 saved in: {result_file2}")
            if len(summary1.keys()) == len(summary2.keys()):
                x1 = [summary1[key]["Correct code"] for key in summary1.keys()]
                mean1= mean(x1)
                x2 = [summary2[key]["Correct code"] for key in summary2.keys()]
                mean2 = mean(x2)
                print(f"Mean1: {mean1}")
                print(f"Mean2: {mean2}")
                print()
                _, p_value = mannwhitneyu(x1, x2, alternative='two-sided')
                if p_value<0.05:
                    print("There is a significant difference")
                else:
                    print("There is no difference")
            else:
                print("The number of experiments is different. We can't perform test")
            return summary1, summary2
        
        ## performance
        elif method == "performance":
            result_file, results = self.test_performance(result1_df, result2_df, result_dir, large_input, timeout)
            print(f"Results saved in: {result_file}")            
            return results, results
            
        else:
            return "Test not supported"
        
    def test_static(self, result_df,  method, result_dir):
        os.makedirs(result_dir, exist_ok=True)
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in tqdm(range(n_rep)):
            result = []
            for i in tqdm(range(len(result_df))):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                # method_name = extract_method_name(code)[0]
                # test = code + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "inef_test": method(code)
                }
                # try:
                #     exec(test)
                #     to_save["correct_code"] = True
                # except:
                #     to_save["correct_code"] = False
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Total raised": len([x for x in result if x["inef_test"]]),
                                # "Correct code raised": len([x for x in result if x["inef_test"] and x["correct_code"]]),
                                # "Incorrect code raised": len([x for x in result if x["inef_test"] and not x["correct_code"]]),
                                }
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
        return result_file, summary
    
    def test_general_logic(self, result_df, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_general_logic_humaneval(result_df, result_dir)
        if self.benchmark_name == "bigcodebench":
            return self.test_general_logic_bigcode_bench(result_df, result_dir)

    def test_general_logic_humaneval(self, result_df, result_dir):
        os.makedirs(result_dir, exist_ok=True)
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in tqdm(range(n_rep)):
            result = []
            for i in tqdm(range(len(result_df))):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                method_name = extract_method_name(code)[0]
                test = code + "\n"+ self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                to_save = {
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
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Correct code": len([x for x in result if not x["correct_code"]])}
            result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
        return result_file, summary
    
    def test_general_logic_bigcode_bench(self, result_df, result_dir):
        os.makedirs(result_dir, exist_ok=True)
        assert len(result_df) == len(self.benchmark)
        n_rep = len([x for x in result_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in range(n_rep):
            result = []
            for i in tqdm(range(len(result_df))):
                task_id = result_df["task_id"][i]
                prompt = result_df["prompt"][i]
                code = result_df[f"exp_{str(j)}"][i]
                test = code + "\n"+ self.benchmark[i]["test"] + f'\nimport io\noutput = io.StringIO()  # Create a StringIO buffer to capture the output\nloader = unittest.TestLoader()\nsuite = loader.loadTestsFromTestCase(TestCases)\nrunner = unittest.TextTestRunner(verbosity=2, stream=output)  # Direct output to the buffer\nrunner.run(suite)\ntest_output = output.getvalue()  # Get the captured output'
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "test": test
                }
                try:
                    to_save["correct_code"] = execute_unittest(test)
                except:
                    to_save["correct_code"] = False
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Correct code": len([x for x in result if not x["correct_code"]])}
            result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
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
                        # difference_count = sum(max(i2 - i1, j2 - j1) for tag, i1, i2, j1, j2 in SequenceMatcher(None, test1, test2).get_opcodes() if tag != "equal")
                        # print(difference_count)

                        # print(test1)
                        # print(test2)
                        # print(time1, time2)
                        # print(mem1, mem2)
                        # exit()
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
    

   
if __name__ == "__main__":
    large_input = False
    timeout = True
    # /workspace/ReCatcher/
    # /workspace/ReCatcher/data
    re_catcher = ReCatcher("/workspace/ReCatcher/data/bigcode/dataset.parquet", test_timeout=45)
    gpt3_5 = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/gpt-3.5-turbo.csv")
    gpt4 = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/gpt-4o.csv")
    gpt4mini = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/gpt-4o-mini.csv")
    
    codellama_base = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/meta-llama_CodeLlama-7b-hf.csv")
    codellama_finetuned = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/JetBrains_CodeLlama-7B-Kexer.csv")
    codellama_merged = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/DevQuasar_coma-7B-v0.1.csv")
    
    deepseek_base = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/deepseek-ai_deepseek-coder-6.7b-base.csv")
    deepseek_finetuned = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/JetBrains_deepseek-coder-6.7B-kexer.csv")
    deepseek_merged = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_bigcodebench/ori-cloud_ds-trinity-7b-v1.csv")
    
    
    # re_catcher = ReCatcher(benchmark="/workspace/ReCatcher/data/humaneval_plus/HumanEvalPlus.jsonl")
    # gpt3_5 = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/gpt-3.5-turbo.csv")
    # gpt4 = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/gpt-4o.csv")
    # gpt4mini = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/gpt-4o-mini.csv")
    
    # codellama_base = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/meta-llama_CodeLlama-7b-hf.csv")
    # codellama_finetuned = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/JetBrains_CodeLlama-7B-Kexer.csv")
    # codellama_merged = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/DevQuasar_coma-7B-v0.1.csv")
    
    # deepseek_base = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/deepseek-ai_deepseek-coder-6.7b-base.csv")
    # deepseek_finetuned = pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/JetBrains_deepseek-coder-6.7B-kexer.csv")
    # deepseek_merged =pd.read_csv("/workspace/ReCatcher/code_generation/results/merged_humaneval_plus/ori-cloud_ds-trinity-7b-v1.csv")
    

    x1, x2 = re_catcher.test_regression(result1_df= codellama_base, result2_df=codellama_finetuned, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    print("codellama base vs finetuned")
    print(x1, x2)
    
    x1, x2 = re_catcher.test_regression(result1_df= codellama_base, result2_df=codellama_merged, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    print("codellama base vs merged")
    print(x1, x2)
    
    # x1, x2 = re_catcher.test_regression(result1_df= deepseek_base, result2_df=deepseek_finetuned, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    # print("deepseek base vs finetuned")
    # print(x1, x2)
    
    # x1, x2 = re_catcher.test_regression(result1_df= deepseek_base, result2_df=deepseek_merged, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    # print("deepseek base vs merged")
    # print(x1, x2)
    
    # x1, x2 = re_catcher.test_regression(result1_df= gpt3_5, result2_df=gpt4, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    # print("gpt 3.5 vs gpt 4")
    # print(x1, x2)
    
    # x1, x2 = re_catcher.test_regression(result1_df= gpt4, result2_df=gpt4mini, method="performance", large_input=large_input, timeout=timeout, result_dir="results")
    # print("gpt 4 vs gpt 4o mini")
    # print(x1, x2)
    