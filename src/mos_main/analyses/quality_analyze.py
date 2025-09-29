import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# Load the CSV file
df = pd.read_csv(r"F:/sharif_Term2/Speech/mos/codes/mos_project/src/mos_main/train/train.csv")
true_col = "score"
pred_col = "mos_pred"

true = df[true_col]
pred = df[pred_col]

# === 2. Define score ranges (bins) with width 0.5 ===
min_score = np.floor(true.min())
max_score = np.ceil(true.max()) + 0.5
bins = np.arange(min_score, max_score, 0.5)

labels = [f"{round(bins[i],2)}-{round(bins[i+1],2)}" for i in range(len(bins)-1)]
df["range"] = pd.cut(true, bins=bins, labels=labels, include_lowest=True)

# === 3. Compute squared error ===
df["sq_error"] = (true - pred) ** 2

# === 4. Group by range to get mean squared error and correlation ===
results = []
for r, group in df.groupby("range"):
    mean_error = group["sq_error"].mean()
    corr = group[true_col].corr(group[pred_col])
    results.append({"range": r, "mean_squared_error": mean_error, "correlation": corr})

results_df = pd.DataFrame(results)

print("\nPerformance per range:")
print(results_df)

# === 5. Plot mean squared error per range ===
plt.figure(figsize=(10,4))
plt.bar(results_df["range"], results_df["mean_squared_error"])
plt.ylabel("Mean Squared Error")
plt.xlabel("True Score Range")
plt.title("MSE per Score Range (Baseline Model)")
plt.xticks(rotation=90)

# Major ticks at 0,1,2,3
#plt.gca().yaxis.set_major_locator(MultipleLocator(1))
# Minor grid at 0.1
plt.gca().yaxis.set_minor_locator(MultipleLocator(.1))
plt.grid(which='minor', linestyle=':', alpha=0.5)  # grid at 0.1
plt.ylim(0, 2.5)  # restrict y axis to 0–3

plt.tight_layout()
plt.show()

# === 6. Plot correlation per range ===
plt.figure(figsize=(10,4))
plt.bar(results_df["range"], results_df["correlation"])
plt.ylabel("Correlation")
plt.xlabel("True Score Range (0.5 width bins)")
plt.title("Correlation per Score Range")
plt.xticks(rotation=90)

plt.gca().yaxis.set_major_locator(MultipleLocator(1))
plt.gca().yaxis.set_minor_locator(MultipleLocator(0.1))
plt.grid(which='minor', linestyle=':', alpha=0.5)
plt.ylim(0, 3)  # restrict y axis to 0–3

plt.tight_layout()
plt.show()
