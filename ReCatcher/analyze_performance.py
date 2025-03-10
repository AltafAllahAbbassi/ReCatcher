from ReCatcher.utils import read_jsonl, write_jsonl_line
from scipy.stats import mannwhitneyu
import json
from collections import Counter
import uuid
import matplotlib.pyplot as plt
import os

def  get_stats_performance(per_results):
    data = read_jsonl(per_results)
    time = []
    memory = []
    n_correct_code = len(data)
    for d in data:
        time.append(d["avg_time"])
        memory.append(d["avg_mem"])
    return {'avg_time': sum(time)/n_correct_code , 'avg_mem': sum(memory)/n_correct_code, 'n_correct_codes': n_correct_code} 

def compare_performance(per_results1, per_results2, result_dir):
    os.makedirs(result_dir, exist_ok=True)
    result_file = os.path.join(result_dir, f"{str(uuid.uuid4())}.jsonl")
    data1 =read_jsonl(per_results1)
    data2 = read_jsonl(per_results2)
    
    n1 = len(data1)
    n2 = len(data2)
    mem_results = []
    time_results = []
    i1 = 0
    i2 = 0
    
    while i1<n1 and i2<n2:
        task_id1 = int(data1[i1]["task_id"].split('/')[-1])
        task_id2 = int(data2[i2]["task_id"].split('/')[-1])
        
        if task_id1 == task_id2:
            mem1 = data1[i1]["memory"]
            mem2 = data2[i2]["memory"]
            
            time1 = data1[i1]["time"]
            time2 = data2[i2]["time"]
            
            
            u_memory, memory_p_value = mannwhitneyu(mem1, mem2, alternative='two-sided')
            u_time, time_p_value = mannwhitneyu(time1, time2, alternative='two-sided')
            
            if memory_p_value<0.05:
                if data1[i1]["avg_mem"] > data2[i2]["avg_mem"]:
                    mem_result = 1 
                else:
                    mem_result = 2
            else:
                mem_result = 0 
            mem_results.append(mem_result)
                
            
            if time_p_value<0.05:
                if data1[i1]["avg_time"] > data2[i2]["avg_time"]:
                    time_result = 1 
                else:
                    time_result = 2
            else:
                time_result = 0
            time_results.append(time_result)
                
            to_save = {
                "task_id": data1[i1]["task_id"], 
                "mem_result" : mem_result, 
                "mem_pvalue": memory_p_value, 
                "mem_u": u_memory,
                "time_result" : time_result,
                "time_pvalue": time_p_value, 
                "time_u": u_time
                
            }
            
            write_jsonl_line(result_file, to_save)
            i1+=1
            i2+=1
        elif task_id1>task_id2:
            i2+=1
        else:
            i1+=1   
    assert len(mem_results) == len(time_results)
    
    print("###############") 
    print(f"results saved in: {result_file}")
    print(f"results from model 1: {per_results1}")
    print(f"results from model 2: {per_results2}")
    print("###############") 
    
    return {
        "n_correct_code": len(mem_results), 
        "memory_overall": Counter(mem_results),
        "time_overall": Counter(time_results) 
    }

def generate_graphs(per_results, save_path):
    data = read_jsonl(per_results)
    mem = [d["avg_mem"] for d in data]
    time = [d["avg_time"] for d in data]
    
    plt.figure(figsize=(8, 5))
    plt.scatter(mem, time, label='Memory vs Time')
    plt.xlabel('Memory Usage (MB)')  # Adjust the label as needed
    plt.ylabel('Execution Time (s)')  # Adjust the label as needed
    plt.title('Memory vs Execution Time')
    plt.legend()
    plt.grid(True)
    # plt.show()
    plt.savefig(save_path, format='pdf', bbox_inches='tight')    



if __name__ == "__main__":

    per_results1 = "" # original model performance results
    per_results2 = "" # variant/new model performance results
    x1 = get_stats_performance(per_results1)
    x2 = get_stats_performance(per_results2)
    print(x1)
    print(x2)
    result = compare_performance(per_results1, per_results2, "path_to_save") 
    print(result)
    