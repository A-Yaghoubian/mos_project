import pandas as pd

# File paths
csv_file1 = "file1.csv"
csv_file2 = "file2.csv"
output_file = "concatenated.csv"

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
