import csv
import json
import os
import time

from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from data.evaluation import constants

### PROMPTS
EVALUATION_PERFORMANCE = """
    Consider you're an expert in Software Engineering with much experience in coding tasks. 
    
    Your task:
    Now, you're asked to evaluate two solutions reported below focusing on performance aspects. 
    For that, you may consider both implementations and analyze them based on time and memory performance.
    
    After your analysis, if there is any difference between them, you have to report which one is the best. If they are the same, just say the solutions are similar. 
    As possible solutions, you must report:
    SOLUTION_ONE, if solution one is the best;
    SOLUTION_TWO, if solution two is the best;
    EQUAL, if the solutions are similar. 
    For your answer, do it using a json format, with one single key: evaluation : "ANSWER"

    Your answer: 
    Provide your answer using a JSON format, with four keys:
    - TIME_EVALUATION, followed by your evaluation. Your answer might be: 
        + SOLUTION_ONE, if solution one is the best;
        + SOLUTION_TWO, if solution two is the best;
        + EQUAL, if the solutions are similar. 
    - REASONING, followed by your explanation to support your decision.
    - MEMORY_EVALUATION, followed by your evaluation. Your answer might be: 
        + SOLUTION_ONE, if solution one is the best;
        + SOLUTION_TWO, if solution two is the best;
        + EQUAL, if the solutions are similar. 
    - REASONING, followed by your explanation to support your decision.
    
    For example: 
    ```json
        {{
            "TIME_EVALUATION" : "YOUR ANSWER",
            "REASONING_TIME" : "YOUR EXPLANATION"
            "MEMORY_EVALUATION" : "YOUR ANSWER",
            "REASONING_MEMORY" : "YOUR EXPLANATION"
        }}
    ```
            
    Solution One:
    {generated_solution_one}
    
    Solution Two:
    {generated_solution_two}
     
"""

EVALUATION_LOGIC = """
    Consider you're an expert in Software Engineering with much experience in coding tasks. 

    Your task:
    Evaluate the correctness of the code implementation below.
    For that, consider the description of the function (informed as comments), the proposed solution, and based on the proposed test assertions, provide your answer.

    Your answer: 
    Provide your answer using a JSON format, with two keys:
    - EVALUATION, followed by your evaluation. Your answer might be: CORRECT or INCORRECT 
    - REASONING, followed by your explanation to support your decision.

    For example: 
    ```json
        {{
            "EVALUATION" : "YOUR ANSWER",
            "REASONING" : "YOUR EXPLANATION"
        }}
    ```

    Task Details:
    {generated_solution}

"""

llm = ChatOpenAI(
    model_name=constants.OPEN_AI_MODEL,
    temperature=constants.TEMPERATURE,
    openai_api_key=constants.OPEN_API_KEY
)

logical_chain = LLMChain(
    prompt=PromptTemplate.from_template(EVALUATION_LOGIC),
    llm=llm
)

performance_chain = LLMChain(
    prompt=PromptTemplate.from_template(EVALUATION_PERFORMANCE),
    llm=llm
)

def save_output_comments(experiment_id, task_id, test_judgment, llm_judment, llm_reasoning, filename_):
    filename = constants.REPORT_FILE_NAME + filename_ + ".csv"
    output_csv_path = os.path.join(constants.REPORT_DIRECTORY, filename)
    try:

        headers = [
            "experiment_id",
            "task_id",
            "test_judgment",
            "llm_judgment",
            "llm_reasoning",
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
                    "experiment_id": experiment_id,
                    "task_id": task_id,
                    "test_judgment": test_judgment,
                    "llm_judgment": llm_judment,
                    "llm_reasoning": llm_reasoning
                }
            )

        print(f"CSV file has been successfully written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_output_performance_comments(experiment_id, task_id, solution_one, solution_two,
        time_evaluation, reasoning_time, memory_evaluation, reasoning_memory):
    filename = constants.REPORT_PERFORMANCE_FILE_NAME + task_id.split("/")[0] + ".csv"
    output_csv_path = os.path.join(constants.REPORT_DIRECTORY, filename)
    try:

        headers = [
            "experiment_id",
            "task_id",
            "solution_one",
            "solution_two",
            "time_evaluation",
            "reasoning_time",
            "memory_evaluation",
            "reasoning_memory",
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
                    "experiment_id": experiment_id,
                    "task_id": task_id,
                    "solution_one": solution_one,
                    "solution_two": solution_two,
                    "time_evaluation": time_evaluation,
                    "reasoning_time": reasoning_time,
                    "memory_evaluation": memory_evaluation,
                    "reasoning_memory": reasoning_memory,
                }
            )

        print(f"CSV file has been successfully written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def extract_and_parse_json(input_string):
    try:
        start_index = input_string.find('{')
        end_index = input_string.rfind('}')

        if start_index == -1 or end_index == -1 or start_index > end_index:
            raise ValueError("Invalid JSON format: Missing or misaligned brackets.")

        json_content = input_string[start_index:end_index + 1]

        parsed_json = json.loads(json_content)
        return parsed_json
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON: {e}")

def evaluate_logic_llm_judger(testing_assertions):
    judgment = logical_chain.invoke({"generated_solution": testing_assertions})["text"]

    if judgment is not None:
        try:
            final_evaluation = extract_and_parse_json(judgment)

            if isinstance(final_evaluation, str):
                report = json.loads(final_evaluation)
            else:
                report = final_evaluation

            return [report.get("EVALUATION"), report.get("REASONING")]
        except Exception as e:
            print(e)
            return None
    return None

def evaluate_performance_llm_judger(solution_one, solution_two):
    judgment = performance_chain.invoke({"generated_solution_one": solution_one, "generated_solution_two": solution_two})["text"]

    if judgment is not None:
        try:
            final_evaluation = extract_and_parse_json(judgment)

            if isinstance(final_evaluation, str):
                report = json.loads(final_evaluation)
            else:
                report = final_evaluation

            return [report.get("TIME_EVALUATION"), report.get("REASONING_TIME"), report.get("MEMORY_EVALUATION"), report.get("REASONING_MEMORY")]
        except Exception as e:
            print(e)
            return None
    return None

def get_correct_code(model):
    temp_dict = {}
    for json_str in model:
        result = json.loads(json_str)
        if result['correct_code'] == True:
            base_exp_id = result['exp']
            task_id = result['task_id']

            if base_exp_id not in temp_dict:
                temp_dict[base_exp_id] = {task_id: result['test']}
            else:
                if task_id not in temp_dict[base_exp_id]:
                    temp_dict[base_exp_id][task_id] = result['test']

    return temp_dict

def run_evaluation_logic():
    for input_file in constants.INPUT_FILES_LOGIC_EVALUATION:
        with open(input_file, 'r') as json_file:
            model_generation = list(json_file)

        filename = os.path.basename(input_file).removesuffix('.jsonl')  # Requires Python 3.9+
        model_name = os.path.basename(os.path.dirname(input_file))
        benchmark_name = os.path.basename(os.path.dirname(os.path.dirname(input_file)))

        for json_str in model_generation:
            try:
                result = json.loads(json_str)
                output = evaluate_logic_llm_judger(result['test'])
                snippet_id = result.get("exp") + "_" + result.get("task_id")
                save_output_comments(snippet_id, result['task_id'], result['correct_code'], output[0], output[1],
                                     "_" + filename + "_" + model_name + "_" + benchmark_name)
                time.sleep(2)
            except Exception as e:
                print(f"Attempt failed: {e}")
                time.sleep(2)  # Fixed 2-second sleep

def run_evaluation_performance():

    for par_files in constants.INPUT_FILES_PERFORMANCE_EVALUATION:
        aux = 0
        with open(par_files[0], 'r') as json_file:
            base_model = get_correct_code(list(json_file))

        with open(par_files[1], 'r') as json_file:
            variant_model = get_correct_code(list(json_file))

        for exp_id_base, base_tasks in base_model.items():
            #if exp_id_base == "exp_0":
            finetuned_tasks = variant_model.get(exp_id_base, None)
            if finetuned_tasks is not None:
                for base_task in base_tasks:
                    if finetuned_tasks.get(base_task, None) is not None:
                        output = evaluate_performance_llm_judger(base_tasks.get(base_task), finetuned_tasks.get(base_task))
                        save_output_performance_comments(exp_id_base, base_task, base_tasks.get(base_task), finetuned_tasks.get(base_task),
                                             output[0], output[1], output[2], output[3])