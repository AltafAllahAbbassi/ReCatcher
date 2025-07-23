import pandas as pd

a_df = pd.read_csv("data/LLM_judger_logic_base_logic_codellama_humanevalplus.csv")
b_df = pd.read_csv("data/LLM_judger_logic_finetuned_logic_codellama_humanevalplus.csv")

def normalize(label):
    label = str(label).strip().lower()
    if label in ["correct", "true", "pass", "passes", "True", "TRUE"]:
        return 1
    elif label in ["incorrect", "false", "fail", "fails", "False", "FALSE"]:
        return 0
    else:
        return None

a_df["llm_score_A"] = a_df["llm_judgment"].map(normalize)
b_df["llm_score_B"] = b_df["llm_judgment"].map(normalize)

merged = pd.merge(
    a_df[["task_id", "llm_score_A"]],
    b_df[["task_id", "llm_score_B"]],
    on="task_id"
)

merged = merged.dropna(subset=["llm_score_A", "llm_score_B"])

correct_A = merged["llm_score_A"].sum()
correct_B = merged["llm_score_B"].sum()
N = len(merged)

relative_improvement = ((correct_B - correct_A) / N) * 100

print("=== Relative Improvement Based on LLM Judgment ===")
print(f"Total Common Tasks (N): {N}")
print(f"Correct by Model A: {correct_A}")
print(f"Correct by Model B: {correct_B}")
print(f"Relative Improvement (B over A): {relative_improvement:.2f}%")
