import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Step 1: Read CSV ===
file_path = "train_english.csv"
df = pd.read_csv(file_path)

# === Step 2: Choose column ===
column = "mos"  # replace with your column name
data = df[column].dropna()

# === Step 3: Define 10 bins from 0 to 5 (step = 0.5) ===
bins = np.arange(0, 5.5, 0.5)  # [0, 0.5, 1.0, ..., 5.0]
labels = [f"{bins[i]}–{bins[i+1]}" for i in range(len(bins)-1)]

# === Step 4: Cut data into bins and compute percentages ===
binned = pd.cut(data, bins=bins, labels=labels, include_lowest=True)
percentages = binned.value_counts(normalize=True).sort_index() * 100

# === Step 5: Plot ===
plt.figure(figsize=(8, 5))
plt.bar(labels, percentages, width=0.5, color='skyblue', edgecolor='black')
plt.title(f"Distribution of english dataset")
plt.xlabel("Range")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
