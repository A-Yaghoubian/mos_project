import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# --- Load CSV ---
csv_path = 'train.csv'
df_full = pd.read_csv(csv_path)

# Keep file_name separately
file_names = df_full['file_name']

# Drop first column (file_name) for training
df = df_full.drop(columns=['file_name'])

# Separate features (all except last column) and target (last column)
X = df.iloc[:, :-1]  # features
y = df.iloc[:, -1]   # label (score)

# Standardize features (important for Lasso)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train/test (keeping track of file_name for test set)
X_train, X_test, y_train, y_test, fn_train, fn_test = train_test_split(
    X_scaled, y, file_names, test_size=0.2, random_state=42
)

# Fit Lasso model
lasso = Lasso(alpha=0.03)  # tune alpha as needed
lasso.fit(X_train, y_train)

# Predict on train and test set
y_train_pred = lasso.predict(X_train)
y_test_pred = lasso.predict(X_test)

# Compute RMSE (just for test set)
rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
print(f"RMSE on test set: {rmse:.4f}")

# --- Print coefficients ---
feature_names = X.columns  # original feature names
coefficients = lasso.coef_

print("\nAll coefficients:")
for name, coef in zip(feature_names, coefficients):
    print(f"{name}: {coef:.4f}")

zero_features = [name for name, coef in zip(feature_names, coefficients) if coef == 0.0]
print("\nFeatures with zero coefficients (eliminated by Lasso):")
print(zero_features if zero_features else "None")

# --- Save file_name, score (true), pred (prediction) for BOTH train and test ---
train_df = pd.DataFrame({
    'file_name': fn_train,
    'score': y_train,
    'pred': y_train_pred
})

test_df = pd.DataFrame({
    'file_name': fn_test,
    'score': y_test,
    'pred': y_test_pred
})

# Concatenate train + test
output_df = pd.concat([train_df, test_df], axis=0).reset_index(drop=True)

output_df.to_csv('lasso_predictions.csv', index=False)
print("\n Saved predictions for train+test to lasso_predictions_all.csv")
