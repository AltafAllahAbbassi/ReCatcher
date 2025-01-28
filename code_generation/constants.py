DO_SAMPLE=True
TOP_K=10
TEMPERATURE=0.1
TOP_P=0.95
MAX_LENGTH=256
MAX_NEW_TOKENS = 1024
GPU_MEMORY_UTILIZATION = 0.95
MAX_TOKENS = 2048
CLASS_EVAL_DATASET = 'ClassEval'
HUMAN_EVAL_DATASET = 'human'
BIGCODEBENCH = "bigcode"
FREQUENCE_PENALITY=0, 
PRESENCE_PENALITY=0

LARGE_INPUT_HUMAN_EVAL = """
Generate an appropriate input for a given Python method signature and docstring that would allow for measuring its time and memory usage effectively.
Ensure the input is complex enough to potentially reflect the time and memory consumption of the code upon execution.
Please return **ONLY** function call with the generated input.

# Notes:
- **Size Consideration**: Remember that inputs should be large but not infinitely large. Keep in mind the memory constraints of a typical system.
- **Data Types**: Make sure to use appropriate data types, e.g., strings, integers, lists, dictionaries, etc., congruent with the intended use of the provided code snippet.
"""

LARGE_INPUT_BIGCODEBENCH = """
Given a method description and its unit tests, generate a Python method call with all necessary configuration steps. Ensure the following:

- The input size is sufficiently large to capture performance differences between two code versions.
- The code can be executed in less than 3 minutes on a standard computer.
- Include all required configurations derived from the unit tests before executing the method call.
- Return **only** Python code.
- Note: Do **NOT** generate code for task_func method. Generate **only** method call with needed configuration.
"""