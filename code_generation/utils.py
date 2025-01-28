import json
import re

def save_json(save_file, object):
    with open(save_file, 'w') as json_file:
        json.dump(object, json_file, indent=4)
    
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as json_file:
        for line in json_file:
            data.append(json.loads(line))
    return data

def add_jsonl_row(save_file, row):
    with open(save_file, 'a') as file:
        file.write(json.dumps(row) + '\n')

def add_jsonl_completion(save_file, model, completion):
    with open(save_file, 'r') as file:
        lines = file.readlines()

    if lines:
        last_object = json.loads(lines[-1].strip())
        if not last_object['result']:
            last_object['result'] = []
        last_object['result'].append({
            "model": model, 
            "result": completion
        })

        updated_last_line = json.dumps(last_object) + '\n'
        lines[-1] = updated_last_line
        with open(save_file, 'w') as file:
            file.writelines(lines)

def add_desc_to_init(desc, class_init):
        class_init_list = class_init.split('\n')
        class_init_list[0] += " \n" + desc
        class_init = '\n'.join(class_init_list)
        return class_init

def get_method_signature(code, method_name):
        method_def_prefix = "def " + method_name + '('
        code_segment = code.split('):')
        for segment in code_segment:
            if method_def_prefix in segment:
                return "    " + segment + "):"
        return ""

def class_eval_generate_prompt(x):
    prompts = []
    class_name = x['class_name']
    methods_info = x['methods_info']
    imports = '\n'.join(x['import_statement'])
    class_init = add_desc_to_init(x['class_description'], x['class_constructor'])
    for method_to_generate in methods_info:
        class_text = imports + '\n' + class_init
        # gather each method's signature to consruct class level skeleton
        for method in methods_info:
            if method['method_name'] == method_to_generate['method_name']:
                continue
            class_text += get_method_signature(method['method_description'], method['method_name']) + "\n        pass\n\n"

        method_name = method_to_generate['method_name']
        inst = f"please complete {method_name} method in the following class {class_name}\n\n"
        class_text_desc = class_text + "\n\n    " + method_to_generate['method_description']
        prompt = inst + class_text_desc 
        prompts.append(prompt)
    return prompts

def human_eval_generate_prompt(x):
    return [x['prompt']]

def extract_python_code(completion):
    python_code_pattern = r"```python(.*?)```"
    match = re.search(python_code_pattern, completion, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def openai_call(prompt, client, model="gpt-4o-mini", temperature=0, max_tokens=4096, top_p=1, frequency_penalty=0, presence_penalty=0, system_prompt = ""):
    response = client.chat.completions.create(
        model=model, 
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ], 
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty, 
        presence_penalty=presence_penalty,
        response_format={
            "type": "text"
        }
        
    )
    x= extract_python_code(response.choices[0].message.content)
    if not x: 
        return response.choices[0].message.content
    return x

def bigcodebench_generate_prompt(x):
    return [x["complete_prompt"]]