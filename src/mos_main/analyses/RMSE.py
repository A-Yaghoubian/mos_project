import pandas as pd
import numpy as np

# === CONFIGURATION ===
csv_path = "merged_english_1000_voices.csv"         # Path to your CSV file
col1 = "mos_pred"            # Name of the first column
col2 = "mos"               # Name of the second column

# === LOAD CSV ===
df = pd.read_csv(csv_path)

# === CHECK COLUMNS EXIST ===
if col1 not in df.columns or col2 not in df.columns:
    raise ValueError(f"Columns '{col1}' and '{col2}' not found in CSV. Found columns: {df.columns.tolist()}")

# === COMPUTE RMSE ===
rmse = np.sqrt(np.mean((df[col1] - df[col2]) ** 2))

print(f"✅ RMSE between '{col1}' and '{col2}' = {rmse:.4f}")
