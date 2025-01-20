BENCHMARKS = {
    "HUMANEVAL_PLUS": "data/humaneval_plus/HumanEvalPlus.jsonl",
    "CLASSEVAL": "data/classeval/ClassEval_data.json", 
    "BIGCODEBENCH": "data/bigcode/dataset.parquet"
}

BENCHMARK_METHOD_CALLS = {
    
}
PMD_COMMAND_TEMPLATE = "/home/altaf/Documents/pmd-dist-7.8.0-bin/pmd-bin-7.8.0/bin/pmd cpd --minimum-tokens={} -d {} -f text --language python"
CODE_DUPLICATION_MIN_COUNT = 10
COMMENT_DUPLICATION_THRESHOLD = 0.9 
COMMENT_DUPLICATION_MIN_COUNT = 4