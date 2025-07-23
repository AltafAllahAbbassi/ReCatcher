import pandas as pd
import numpy as np
from scipy.stats import wilcoxon, ttest_rel, shapiro

# === Load Data ===
a_df = pd.read_csv("data/ALL_static_analysis_humanevalplus_codellama_base_logic.csv")
b_df = pd.read_csv("data/ALL_static_analysis_humanevalplus_codellama_finetuned_logic.csv")

# === Merge by snippet_id ===
merged = pd.merge(a_df, b_df, on="snippet_id", suffixes=("_A", "_B"))

# === Metrics to compare ===
metrics = [
    "cc_total", "mi"
]

summary = []

for metric in metrics:
    x = merged[f"{metric}_A"]
    y = merged[f"{metric}_B"]

    diff = y - x
    diff = diff.dropna()

    if diff.empty or np.all(diff == 0):
        summary.append({
            "metric": metric,
            "mean_A": round(x.mean(), 2),
            "mean_B": round(y.mean(), 2),
            "Δ (abs)": None,
            "Δ (%)": None,
            "test": "n/a",
            "p-value": "n/a",
            "significant": "",
            "r-size" : ""
        })
        continue

    try:
        stat_norm, p_norm = shapiro(diff)

        print(p_norm, stat_norm)
        if p_norm > 0.05:
            stat, p = ttest_rel(x, y, nan_policy='omit')
            test_type = "paired t-test"
        else:
            stat, p = wilcoxon(x, y)
            test_type = "Wilcoxon"

            n = len(x)
            mean_rank = n * (n + 1) / 4
            std_rank = np.sqrt(n * (n + 1) * (2 * n + 1) / 24)
            z = (stat - mean_rank) / std_rank
            r = abs(z) / np.sqrt(n)

        median_x = x.median()
        median_y = y.median()
        delta_abs = median_y - median_x
        delta_pct = (delta_abs / median_x) * 100 if median_x != 0 else float("nan")

        summary.append({
            "metric": metric,
            "meean_A": round(median_x, 2),
            "mean_B": round(median_y, 2),
            "Δ (abs)": round(delta_abs, 2),
            "Δ (%)": round(delta_pct, 2),
            "test": test_type,
            "p-value": p,
            "significant": "✓" if p < 0.05 else "",
            "r-size" : r
        })

    except Exception as e:
        summary.append({
            "metric": metric,
            "median_A": "error",
            "median_B": "error",
            "Δ (abs)": "error",
            "Δ (%)": "error",
            "test": "error",
            "p-value": "error",
            "significant": "error"
        })
        print(f"Error analyzing {metric}: {e}")

summary_df = pd.DataFrame(summary)
print(summary_df.to_string(index=False))
summary_df.to_csv("metric_significance_summary_full.csv", index=False)
