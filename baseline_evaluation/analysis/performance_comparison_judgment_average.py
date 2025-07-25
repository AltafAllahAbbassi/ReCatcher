import pandas as pd

# List of input files
input_files = [
    "data/LLM_judger_performanceHumanEval.csv",
    "data/LLM_judger_performance_twoHumanEval.csv",
    "data/LLM_judger_performance_threeHumanEval.csv",
    "data/LLM_judger_performance_fourHumanEval.csv",
    "data/LLM_judger_performance_fiveHumanEval.csv"
]

total_counts = {"time": 0, "memory": 0}
sum_count_one = {"time": 0, "memory": 0}
sum_count_two = {"time": 0, "memory": 0}
sum_count_equal = {"time": 0, "memory": 0}

for file in input_files:
    df = pd.read_csv(file)

    df["time_evaluation"] = df["time_evaluation"].str.strip().str.upper()
    df["memory_evaluation"] = df["memory_evaluation"].str.strip().str.upper()

    for col, label in [("time_evaluation", "time"), ("memory_evaluation", "memory")]:
        total = df[col].isin(["SOLUTION_ONE", "SOLUTION_TWO", "EQUAL"]).sum()
        count_one = (df[col] == "SOLUTION_ONE").sum()
        count_two = (df[col] == "SOLUTION_TWO").sum()
        count_equal = (df[col] == "EQUAL").sum()

        total_counts[label] += total
        sum_count_one[label] += count_one
        sum_count_two[label] += count_two
        sum_count_equal[label] += count_equal

def report_average(label):
    total = total_counts[label]
    count_one = sum_count_one[label]
    count_two = sum_count_two[label]
    count_equal = sum_count_equal[label]
    delta = count_two - count_one
    relative_improvement = (delta / total) * 100 if total > 0 else 0

    print(f"\n=== {label.capitalize()} Evaluation (Average Across Files) ===")
    print(f"Total Comparisons: {total}")
    print(f"SOLUTION_ONE better: {count_one}")
    print(f"SOLUTION_TWO better: {count_two}")
    print(f"EQUAL: {count_equal}")
    print(f"Relative Improvement (SOLUTION_TWO over ONE): {relative_improvement:.2f}%")

report_average("time")
report_average("memory")
