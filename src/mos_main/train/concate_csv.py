import pandas as pd
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
print(PROJECT_ROOT)
csv_file1 = "mfcc_features_1000.csv"

csv_file2 = PROJECT_ROOT / "analyses"/ "merged_english_1000_converted_voices.csv"

output_file = "train.csv"

# Load CSVs
df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)
# Check if first column is identical
if not df1.iloc[:, 0].equals(df2.iloc[:, 0]):
    raise ValueError("The first column of the two CSV files is not the same!")

# Concatenate columns (skip the first column of df2 to avoid duplicate)
df_combined = pd.concat([df1, df2.iloc[:, 1:]], axis=1)
# Save to new CSV
df_combined.to_csv(output_file, index=False)

print(f"CSV files concatenated successfully into {output_file}")
