import os 
from openai import OpenAI 
import uuid
import re
import pandas as pd
from tqdm import tqdm
from utils import add_jsonl_completion, add_jsonl_row, openai_call, save_json, human_eval_generate_prompt, read_jsonl, openai_call, bigcodebench_generate_prompt
from constants import TEMPERATURE, MAX_TOKENS, TOP_P, FREQUENCE_PENALITY, PRESENCE_PENALITY, BIGCODEBENCH, HUMAN_EVAL_DATASET

    
model = "gpt-4o"
# model = "gpt-3.5-turbo"
# model = "gpt-4o-mini"
    
datasets = [
    # 'path to bigcodebench'
    ]


client = OpenAI(api_key = "YOUR OPENAI KEY")
    
for dataset in datasets:
        
        for i in range(10):
            
            result_dir = os.path.join("code_generation", "results",  "bigcodebench", "gpt", f"{model}", str(uuid.uuid4()))
            os.makedirs(os.path.join(result_dir))
            config_file = os.path.join(result_dir, 'config.json')
            result_file =  os.path.join(result_dir, 'result.json')            
            exp_config = {
                                    'dataset': dataset,
                                    'task': 'code_completion',
                                    'generation_config': {
                                        # 'do_sample': DO_SAMPLE,
                                        # 'top_k': TOP_K, 
                                        # 'temperature': TEMPERATURE, 
                                        # 'top_p': TOP_P, 
                                        # 'max_length': MAX_LENGTH
                                    }
                            }
            save_json(save_file=config_file,object=exp_config)
            
            if "humaneval" in dataset:
                generate_prompt = human_eval_generate_prompt
                data_inputs = read_jsonl(dataset)
                task_id_ = "task_id"
            
            elif "bigcode" in dataset:
                generate_prompt = bigcodebench_generate_prompt
                df = pd.read_parquet(dataset)
                data_inputs = df.to_dict(orient="records")
                task_id_ = "task_id"
                
            else:
                exit()
                
            for i in tqdm(range(len(data_inputs)),  desc="Processing data"):
                input_ = data_inputs[i]
                input_id = input_[task_id_]
                prompts = generate_prompt(input_)
                for prompt in prompts:
                    to_save_row = {
                        "task_id": input_id, 
                        "prompt": prompt, 
                        "result": []
                        
                    }
                    add_jsonl_row(result_file, to_save_row)

                    completion = openai_call(client=client, prompt=prompt, model=model, temperature=TEMPERATURE, max_tokens=MAX_TOKENS)
                    add_jsonl_completion(result_file, model=model, completion=completion)
            