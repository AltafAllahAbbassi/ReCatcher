import os 
import json 
import pandas as pd
import argparse
from tqdm import tqdm
from openai import OpenAI
from utils import save_json
from constants import JUDGE_FREQUENCY_PENALITY, JUDGE_MAX_TOKENS, JUDGE_MODEL_NAME, JUDGE_PRESENCE_PENALITY, JUDGE_TEMPERATURE, JUDGE_TOP_P, SYSTEM_PROMPT, USER_PROMPT


def judge(client, prompt, code):
    completion = client.chat.completions.create(
        model=JUDGE_MODEL_NAME,
        messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT.format(prompt, code)}
            ], 
        temperature=JUDGE_TEMPERATURE,
        max_tokens=JUDGE_MAX_TOKENS,
        top_p=JUDGE_TOP_P,
        frequency_penalty=JUDGE_FREQUENCY_PENALITY,
        presence_penalty=JUDGE_PRESENCE_PENALITY,
        response_format={
                    "type": "json_object"
            }
            )
    try:
        
        return json.loads(completion.choices[0].message.content.replace("\\n", "\n").replace("\\'", "'"))
    except: 
        return completion.choices[0].message.content

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--judg_number', default=4)
    args = parser.parse_args()
    
    
    gen_results = [ 
        'benchamrk/results/humaneval_deepseek',
        'benchamrk/results/humaneval_gemma', 
        'benchamrk/results/huamaneval_codellama'
    ]

    client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
    
    for gen_result in gen_results:
        csv_file = os.path.join(gen_result, 'result.csv')
        csv_data = pd.read_csv(csv_file,header= 0)
        prompts= csv_data['prompt']
        codes = csv_data['extarcted_method']
        judgements = []
        for i in tqdm(range(len(prompts))):
            prompt = prompts[i]
            code = codes[i]
            judgement = judge(client=client, prompt=prompt, code=code)
            judgements.append(judgement)
        csv_data['judgements_'+ str(args.judg_number)] = judgements 
        csv_data.to_csv(csv_file, index=False)
        judge_config = {
            'model_name': JUDGE_MODEL_NAME, 
            'system_prompt': SYSTEM_PROMPT, 
            'user_prompt': USER_PROMPT, 
            'temperature': JUDGE_TEMPERATURE,
            'max_tokens': JUDGE_MAX_TOKENS,
            'top_p': JUDGE_TOP_P, 
            'presence_penality': JUDGE_PRESENCE_PENALITY, 
            'frequency_penality': JUDGE_FREQUENCY_PENALITY
            
             }
        save_json(save_file = os.path.join(gen_result, 'judge_config.json'), object=judge_config)