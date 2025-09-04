import pandas as pd
import numpy as np
from scipy.stats import pearsonr

# Adjust paths if needed
pred_path = "data/results/predictions.csv"
gt_path = "data/ground_truth.csv"  # You must create/collect this manually

pred = pd.read_csv(pred_path)
gt = pd.read_csv(gt_path)

print("Prediction columns:", pred.columns)
print("Ground truth columns:", gt.columns)

df = pd.merge(gt, pred, left_on="filepath_deg", right_on="file", how="inner")
pearson, _ = pearsonr(df["mos"], df["prediction"])
rmse = np.sqrt(((df["mos"] - df["prediction"]) ** 2).mean())

print(f"Pearson r = {pearson:.4f}, RMSE = {rmse:.4f}")
