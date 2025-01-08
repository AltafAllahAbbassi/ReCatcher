import os
import uuid
from collections import Counter
from scipy.stats import mannwhitneyu
from statistics import mean
from tqdm import tqdm
from ReCatcher.utils import unnecessary_conditional_block, unnecessary_else, variable_naming, sub_readable, syntax_error, missing_import_declaration, code_duplication, comment_duplication
from ReCatcher.utils import read_jsonl, extract_method_name, save_json, measure_execution_performance
from ReCatcher.constants import BENCHMARKS

class ReCatcher(object):
    def __init__(self, benchmark=BENCHMARKS["HUMANEVAL_PLUS"], benchmark_method_call = "/home/altaf/Desktop/ReCatcher/data/humaneval_plus/humaneval_method_call.jsonl", n_rep = 10):
        # if benchmark == BENCHMARKS["HUMANEVAL_PLUS"]:
            self.benchmark = read_jsonl(benchmark)
            self.benchmark_name = "humaneval"
            self.benchmark_large_inputs = read_jsonl(benchmark_method_call)
            self.n_rep = 10 # how many times we repeat the execution for perforamnce

    def test_regression(self, result1_df, result2_df, method, result_dir):
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
        elif method == "compare_performance":
            result_file, results = self.test_performance(result1_df, result2_df, result_dir)
            print(f"Results saved in: {result_file}")

            counter_time = [dict(Counter(results[key]["time"])) for key in results.keys()]
            counter_memory = [dict(Counter(results[key]["memory"])) for key in results.keys()]
            
            counter_time1 = [counter_time[i].get(1, 0) for i in range(len(counter_time))]
            counter_time2 = [counter_time[i].get(2, 0) for i in range(len(counter_time))]

            
            
            counter_memory1 = [counter_memory[i].get(1, 0) for i in range(len(counter_memory))]
            counter_memory2 = [counter_memory[i].get(2, 0) for i in range(len(counter_memory))]
            _, time_p_value = mannwhitneyu(counter_time1, counter_time2, alternative='two-sided')
            _, memory_p_value = mannwhitneyu(counter_memory1, counter_memory2, alternative='two-sided')
            
            if time_p_value<0.05:
                print("There is a significant difference in time")
                print(mean(counter_time1))
                print(mean(counter_time2))
            else:
                print("There is no a significant difference in time")
                
                
            if memory_p_value<0.05:
                print("There is a significant difference in memory")
                print(mean(counter_memory1))
                print(mean(counter_memory2))
            else:
                print("There is no a significant difference in memory")
            
            return results, results
            
        else:
            return "Test not supported"
        
    def test_static(self, result_df,  method, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_static_humaneval(result_df, method, result_dir)
    
    def test_static_humaneval(self, result_df, method, result_dir):
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
                test = code + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                to_save = {
                    "task_id": task_id,
                    "prompt": prompt,
                    "code": code,
                    "inef_test": method(code)
                }
                try:
                    exec(test)
                    to_save["correct_code"] = True
                except:
                    to_save["correct_code"] = False
                result.append(to_save)
            results[f"exp_{j}"] = result
            summary[f"exp_{j}"] = {"Total raised": len([x for x in result if x["inef_test"]]),
                                "Correct code raised": len([x for x in result if x["inef_test"] and x["correct_code"]]),
                                "Incorrect code raised": len([x for x in result if x["inef_test"] and not x["correct_code"]]),
                                }
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
        return result_file, summary
    
    def test_general_logic(self, result_df, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_general_logic_humaneval(result_df, result_dir)

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
    
    def test_performance(self, result1_df, result2_df, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_performance_human_eval(result1_df, result2_df, result_dir)
    
    def test_performance_human_eval(self, result1_df, result2_df, result_dir):
        if self.benchmark_name == "humaneval":
            return self.test_performance_human_eval(result1_df, result2_df, result_dir)

    def test_performance_human_eval(self, result1_df, result2_df, result_dir):
        # if I Have number 1, this means code 1 is worse
        assert len(result1_df) == len(self.benchmark) == len(result2_df)
        n_rep = len([x for x in result1_df.columns if x.startswith("exp")])
        results = {}
        summary = {}
        for j in tqdm(range(n_rep)):
            result = []
            overall_result_time = []
            overall_result_memory = []
            for i in tqdm(range(len(result1_df))):
                task_id = result1_df["task_id"][i]
                prompt = result1_df["prompt"][i]
                code1 = result1_df[f"exp_{str(j)}"][i]
                code2 = result2_df[f"exp_{str(j)}"][i]
                method_name = extract_method_name(code1)[0]
                test1 = code1 + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                test2 = code2 + self.benchmark[i]["test"] + "\n" + f"check({method_name})"
                method_call =  self.benchmark_large_inputs[i]["method_call"]
                try:
                    exec(test1)
                    exec(test2)
                    per1 = measure_execution_performance(code=code1, method_call=method_call, n_repetition=self.n_rep)
                    per2 = measure_execution_performance(code=code2, method_call=method_call, n_repetition=self.n_rep)
                    if not(per1["execution_time"] =="FAIL" or per2["execution_time"] =="FAIL" or per1["memory_usage"] =="FAIL" or per1["memory_usage"] =="FAIL"):
                        time1 =  per1["execution_time"]
                        time2 = per2["execution_time"]
                        mem1 = per1["memory_usage"]
                        mem2 = per2["memory_usage"]
                        
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
                        overall_result_time.append(time)
                        overall_result_memory.append(memory)
                        
                        to_save = {
                        "task_id": task_id,
                        "prompt": prompt,
                        "code1": code1,
                        "code2": code2,
                        "test": self.benchmark[i]["test"], 
                        "method_call": method_call, 
                        "code1_per": per1, 
                        "code2_per": per2
                        }
                        result.append(to_save)
                except:
                    pass
            results[f"exp_{j}"] = result
            summary[f'exp_{j}'] = {"time": overall_result_time, "memory": overall_result_memory}
        result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.json")
        save_json(result_file, results)
        return  result_file, summary
            
    
if __name__ == "__main__":
    re_catcher = ReCatcher()
    result_dir = "Examples/results"
    import pandas as pd 
    results1_df = pd.read_csv("/home/altaf/Desktop/ReCatcher/code_generation/results/merged_humaneval_plus/deepseek-ai_deepseek-coder-6.7b-base.csv")
    results2_df = pd.read_csv("/home/altaf/Desktop/ReCatcher/code_generation/results/merged_humaneval_plus/JetBrains_deepseek-coder-6.7B-kexer.csv")
    x,y = re_catcher.test_performance_human_eval(results1_df, results2_df, result_dir)

    counter_time = [dict(Counter(y[key]["time"])) for key in y.keys()]
    counter_memory = [dict(Counter(y[key]["memory"])) for key in y.keys()]
    
    counter_time1 = [counter_time[i].get(1, 0) for i in range(len(counter_time))]
    counter_time2 = [counter_time[i].get(2, 0) for i in range(len(counter_time))]

    
    
    counter_memory1 = [counter_memory[i].get(1, 0) for i in range(len(counter_memory))]
    counter_memory2 = [counter_memory[i].get(2, 0) for i in range(len(counter_memory))]
    _, time_p_value = mannwhitneyu(counter_time1, counter_time2, alternative='two-sided')
    _, memory_p_value = mannwhitneyu(counter_memory1, counter_memory2, alternative='two-sided')
    
    if time_p_value<0.05:
        print("There is a significant difference in time")
        print(mean(counter_time1))
        print(mean(counter_time2))
    else:
        print("There is no a significant difference in time")
        
        
    if memory_p_value<0.05:
        print("There is a significant difference in memory")
        print(mean(counter_memory1))
        print(mean(counter_memory2))
    else:
        print("There is no a significant difference in memory")
    
    
    

    
    
    