import os 
import uuid
from tqdm import tqdm
import torch
import transformers
from transformers import AutoTokenizer
from huggingface_hub import login
from dotenv import load_dotenv
from constants import DO_SAMPLE, TOP_K, TEMPERATURE, TOP_P, MAX_LENGTH, MAX_NEW_TOKENS, HUMAN_EVAL_DATASET, CLASS_EVAL_DATASET
from utils import save_json, read_jsonl, add_jsonl_completion, add_jsonl_row, human_eval_generate_prompt, class_eval_generate_prompt, read_json

load_dotenv()
hf_token = os.getenv('HF_TOEKN')
login(hf_token)

def complete_code(tokenizer, pipeline, prompt ):
    sequences = pipeline(
        prompt,
        do_sample=DO_SAMPLE,
        top_k=TOP_K,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
        max_new_tokens=MAX_NEW_TOKENS
        # max_length=MAX_LENGTH,
        )
    return sequences[0]['generated_text']
    

if __name__ == '__main__':
    
    if torch.cuda.is_available():
        print(f"Using GPU: {torch.cuda.get_device_name(0)}")
    else:
        print("Using CPU")
               
    
    
    model = 'deepseek-ai/deepseek-coder-6.7b-base' 
    # model = 'DevQuasar_coma-7B-v0.1'
    # mdoel = 'JetBrains_CodeLlama-7B-Kexer'
    # model = 'JetBrains_deepseek-coder-6.7B-kexer'
    # model = 'meta-llama_CodeLlama-7b-hf'
    # model = 'ori-cloud_ds-trinity-7b-v1'

    datasets = [ 
                # 'dataset/humaneval+/HumanEvalPlus.jsonl', 
                ]
    
    result_folder = ""
    os.makedirs(result_folder, exist_ok=True)
    tokenizer = AutoTokenizer.from_pretrained(model)

    device = 0 if torch.cuda.is_available() else -1
    pipeline = transformers.pipeline(
                            "text-generation",
                            model=model,
                            torch_dtype=torch.float16,
                            device=device,
                        )   
    
    for i in range(10):
        for dataset in datasets:  
            # prepare experience output folder per dataset
            # config.json: contains the the configuration of the experience
            # results.json: contains the results structured as follows:
            #   task_id
            #   prompt
            #   result
            #       model
            #       completion 
            result_folder = os.path.join('results', 'code_completion', f'{model}', f'{dataset}')
            exp_result = os.path.join(result_folder, str(uuid.uuid4()))
            os.makedirs(os.path.join(exp_result))
            config_file = os.path.join(exp_result, 'config.json')
            result_file =  os.path.join(exp_result, 'result.json')            
            exp_config = {
                        'dataset': dataset,
                        'task': 'code_completion',
                        'generation_config': {
                            'do_sample': DO_SAMPLE,
                            'top_k': TOP_K, 
                            'temperature': TEMPERATURE, 
                            'top_p': TOP_P, 
                            'max_length': MAX_LENGTH
                        }
                }
            save_json(save_file=config_file,object=exp_config)
            
            if CLASS_EVAL_DATASET in dataset:
                generarate_prompt = class_eval_generate_prompt
                data_inputs = read_json(dataset)
                task_id_ = 'task_id'
                
            elif HUMAN_EVAL_DATASET in dataset:
                generarate_prompt = human_eval_generate_prompt
                data_inputs = read_jsonl(dataset)   
                task_id_ = 'task_id'
                
            else:
                exit()
                
            for i in tqdm(range(len(data_inputs)),  desc="Processing data"):
                input_ = data_inputs[i]
                input_id = input_[task_id_]
                prompts = generarate_prompt(input_)
                for prompt in prompts:
                    to_save_row = {
                        "task_id": input_id, 
                        "prompt": prompt, 
                        "result": []
                        
                    }
                    add_jsonl_row(result_file, to_save_row)

                    completion = complete_code(tokenizer=tokenizer, pipeline=pipeline, prompt=prompt)
                    add_jsonl_completion(result_file, model=model, completion=completion)

                

