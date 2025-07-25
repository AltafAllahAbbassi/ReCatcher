import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    matthews_corrcoef,
    classification_report
)

# === Load CSV ===
df = pd.read_csv("data/LLM_judger_logic_base_finetuned_logic_codellama_humanevalplus.csv")

# === Normalize values ===
# You can adjust these mappings if you use different terms (e.g., "Correct", "Pass", etc.)
def normalize_label(label):
    label = str(label).strip().lower()
    if label in ["correct", "true", "pass", "passes", "True", "TRUE", "CORRECT"]:
        return 1
    elif label in ["incorrect", "false", "fail", "fails", "False", "FALSE", "INCORRECT"]:
        return 0
    else:
        return None  # skip unknown labels

df["y_true"] = df["test_judgment"].map(normalize_label)
df["y_pred"] = df["llm_judgment"].map(normalize_label)

# === Drop invalid rows ===
df_clean = df.dropna(subset=["y_true", "y_pred"])

y_true = df_clean["y_true"]
y_pred = df_clean["y_pred"]

# === Compute Metrics ===
print("=== LLM Judgment Evaluation ===")
print(f"Total Evaluated Samples: {len(df_clean)}\n")

print("Confusion Matrix:")
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(f"  TP: {tp}, FP: {fp}, FN: {fn}, TN: {tn}\n")

print("Scores:")
print(f"  Accuracy : {accuracy_score(y_true, y_pred):.4f}")
print(f"  Precision: {precision_score(y_true, y_pred):.4f}")
print(f"  Recall   : {recall_score(y_true, y_pred):.4f}")
print(f"  F1 Score : {f1_score(y_true, y_pred):.4f}")
print(f"  MCC      : {matthews_corrcoef(y_true, y_pred):.4f}\n")

print("Detailed Report:")
print(classification_report(y_true, y_pred, target_names=["Incorrect", "Correct"]))
