JUDGE_SYSTEM_PROMPT  = "You are a Python expert with a focus on detailed code quality assessment.\n\n" \
"The user will provide you with two Python code snippets implementing the same method. Your objective is to identify any regressions in code quality aspects between the two provided codes, focusing on how Code 2 may have regressed compared to Code 1. Please follow these steps:\n\n" \
"1. Thoroughly analyze the given code snippets.\n" \
"2. Identify specific code quality aspects where Code 2 has regressed compared to Code 1.\n" \
"3. **Only include aspects where Code 2 is significantly worse than Code 1.** Do not include aspects where Code 2 is similar or better, or where differences are insignificant.\n" \
"4. For each identified regression, provide an explanation of how Code 2 has regressed.\n" \
"5. Provide the final output in JSON format, including only the aspects where regressions were found.\n\n" \
"Please structure the JSON output as follows:\n" \
"{\n  \"Detailed Answer\": {\n    \"{Identified Aspect}\": \"{Explanation of the Regression}\",\n  },\n  \"Conclusion\": {\n    \"{Identified Aspect}\"}"


JUDGE_USER_PROMPT = "Please analyze the following two Python code snippets, both implementing the same method:\n" \
"- Code 1: {}\n" \
"- Code 2: {}\n\n" \
"Compare them with a focus on identifying any regressions in code quality aspects in Code 2 compared to Code 1. " \
"Report only the significant regressions where Code 2 is worse than Code 1. " \
"Omit aspects where Code 2 is similar to Code 1, or where the differences are insignificant."



JUDGE_MODEL_NAME = "gpt-4o-mini"

JUDGE_TEMPERATURE = 0.0 
JUDGE_MAX_TOKENS = 5120
JUDGE_TOP_P = 1
JUDGE_FREQUENCY_PENALITY = 0
JUDGE_PRESENCE_PENALITY = 0