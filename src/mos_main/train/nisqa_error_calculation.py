import pandas as pd
import numpy as np

# Path to your CSV file
csv_path = 'train.csv'

# Load CSV but ignore first column (file name)
df = pd.read_csv(csv_path)

# If first column is actually file name and the next two are mos_pred and score:
# (If your CSV looks like: file_name,mos_pred,score)
# then we simply do:
df_200 = df.head(200)  # take first 200 rows

# Compute RMSE between mos_pred and score
rmse = np.sqrt(((df_200['mos_pred'] - df_200['score']) ** 2).mean())

print(f"RMSE for first 200 files: {rmse:.4f}")
