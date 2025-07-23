import pandas as pd
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

llm_files = [
    "data/LLM_judger_performanceHumanEval.csv",
    "data/LLM_judger_performance_twoHumanEval.csv",
    "data/LLM_judger_performance_threeHumanEval.csv",
    "data/LLM_judger_performance_fourHumanEval.csv",
    "data/LLM_judger_performance_fiveHumanEval.csv",
]

run_df = pd.read_csv("data/performance_analysis_codellama_HumanEval.csv")
run_df = run_df.rename(columns={"exp_id": "experiment_id"})

merged_dfs = []
for llm_file in llm_files:
    llm_df = pd.read_csv(llm_file)
    merged = pd.merge(llm_df, run_df, on=["experiment_id", "task_id"], how="inner")
    merged_dfs.append(merged)

df = pd.concat(merged_dfs, ignore_index=True)

df["time_evaluation"] = df["time_evaluation"].str.strip().str.upper()
df["memory_evaluation"] = df["memory_evaluation"].str.strip().str.upper()

eval_map = {
    "SOLUTION_ONE": "CODE_BASE",
    "SOLUTION_TWO": "CODE_VARIANT",
    "EQUAL": "EQUAL"
}

df["time_pred"] = df["time_evaluation"].map(eval_map)
df["memory_pred"] = df["memory_evaluation"].map(eval_map)
df["time_true"] = df["evaluation_time"]
df["memory_true"] = df["evaluation_memory"]

df = df.dropna(subset=["time_pred", "memory_pred", "time_true", "memory_true"])

print("=== TIME CLASSIFICATION REPORT ===")
print(classification_report(df["time_true"], df["time_pred"], zero_division=0))

print("=== MEMORY CLASSIFICATION REPORT ===")
print(classification_report(df["memory_true"], df["memory_pred"], zero_division=0))

def print_overall_metrics(y_true, y_pred, label="TIME"):
    print(f"\n=== OVERALL {label} METRICS ===")
    print(f"Accuracy              : {accuracy_score(y_true, y_pred):.4f}")
    print(f"Precision (macro)     : {precision_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    print(f"Recall    (macro)     : {recall_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    print(f"F1-score  (macro)     : {f1_score(y_true, y_pred, average='macro', zero_division=0):.4f}")
    print(f"Precision (micro)     : {precision_score(y_true, y_pred, average='micro', zero_division=0):.4f}")
    print(f"Recall    (micro)     : {recall_score(y_true, y_pred, average='micro', zero_division=0):.4f}")
    print(f"F1-score  (micro)     : {f1_score(y_true, y_pred, average='micro', zero_division=0):.4f}")
    print(f"Precision (weighted)  : {precision_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")
    print(f"Recall    (weighted)  : {recall_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")
    print(f"F1-score  (weighted)  : {f1_score(y_true, y_pred, average='weighted', zero_division=0):.4f}")

print_overall_metrics(df["time_true"], df["time_pred"], label="TIME")
print_overall_metrics(df["memory_true"], df["memory_pred"], label="MEMORY")