
#For the input files, please, download and unzip the required files from https://zenodo.org/records/14997627

INPUT_FILES_LOGIC_EVALUATION = ["../testing_results/testing_results/humanevalplus/codellama/base_logic.jsonl",
                                "../testing_results/testing_results/humanevalplus/codellama/finetuned_logic.jsonl",
                                ]

INPUT_FILES_PERFORMANCE_EVALUATION = [["../testing_results/testing_results/humanevalplus/codellama/base_logic.jsonl",
                                       "../testing_results/testing_results/humanevalplus/codellama/finetuned_logic.jsonl"]]
OPEN_AI_MODEL = "gpt-4o-mini"
TEMPERATURE = 0.2
OPEN_API_KEY = ""
REPORT_DIRECTORY = "results/"
REPORT_FILE_NAME = "LLM_judger_logic"
REPORT_PERFORMANCE_FILE_NAME = "LLM_judger_performance_"
REPORT_PERFORMANCE = "performance_analysis_codellama_"