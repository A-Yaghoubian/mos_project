import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# --- Load merged CSV ---
merged_csv = 'merged_predictions.csv'  # contains: file_name, score, pred_lasso, pred_rag
df = pd.read_csv(merged_csv)

# Features: pred_lasso and pred_rag
X = df[['pred_lasso', 'pred_rag']].values
y = df['score'].values

# --- Fit linear regression ---
linreg = LinearRegression()
linreg.fit(X, y)

# Get coefficients and intercept
coef_lasso, coef_rag = linreg.coef_

intercept = linreg.intercept_
print(f"Linear Regression Coefficients: pred_lasso={coef_lasso:.4f}, pred_rag={coef_rag:.4f}")
print(f"Intercept: {intercept:.4f}")

# --- Predict final score ---
df['final_pred'] = linreg.predict(X)
# --- Compute RMSE ---
rmse = np.sqrt(mean_squared_error(df['score'], df['final_pred']))
print(f"✅ RMSE of combined predictions: {rmse:.4f}")

# --- Save updated CSV ---
df.to_csv('merged_predictions_final.csv', index=False)
print("✅ Saved merged CSV with final predictions to merged_predictions_final.csv")
