import pandas as pd

# Load the CSV file
df = pd.read_csv(r"merged_english_1000_converted_voices.csv")

# Replace with your actual column names
col1 = "mos"       # for example
col2 = "mos_pred"  # for example

# Compute correlation (Pearson by default)
corr = df[col1].corr(df[col2])

print(f"Correlation between {col1} and {col2}: {corr}")
