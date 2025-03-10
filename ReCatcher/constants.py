BENCHMARKS = {
    "HUMANEVAL_PLUS": "dataset/humaneval_plus/HumanEvalPlus.jsonl",
    "BIGCODEBENCH": "dataset/bigcode/dataset.parquet"
}


# duplication tests configuration 
PMD_COMMAND_TEMPLATE = "/pmd-bin-7.8.0/bin/pmd cpd --minimum-tokens={} -d {} -f text --language python"
CODE_DUPLICATION_MIN_COUNT = 10
COMMENT_DUPLICATION_THRESHOLD = 0.9 
COMMENT_DUPLICATION_MIN_COUNT = 4