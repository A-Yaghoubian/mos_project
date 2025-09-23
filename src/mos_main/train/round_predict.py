import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- Load merged CSV ---
merged_csv = 'merged_predictions_final.csv'  # the file with final_pred
df = pd.read_csv(merged_csv)

# --- Function to clip and round to nearest 0.5 ---
def clip_and_round_half(x):
    x = max(1.0, min(5.0, x))  # clip to [1, 5]
    return round(x * 2) / 2     # round to nearest 0.5

# --- Apply function to final_pred ---
df['final_pred_rounded'] = df['final_pred'].apply(clip_and_round_half)

# --- Optionally compute RMSE for rounded predictions ---
rmse_rounded = np.sqrt(mean_squared_error(df['score'], df['final_pred_rounded']))
print(f"RMSE of rounded predictions: {rmse_rounded:.4f}")

# --- Save updated CSV ---
df.to_csv('merged_predictions_final_rounded.csv', index=False)
print("Saved CSV with rounded final predictions to merged_predictions_final_rounded.csv")
