import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

# --- Load CSV ---
csv_path = 'train.csv'  # contains file_name, features..., score
df = pd.read_csv(csv_path)

file_names = df['file_name']        # keep file names
scores = df['score'].values         # true scores (label)

# Drop file_name and score to get features
X = df.drop(columns=['file_name', 'score'])

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- Fit Lasso to select features ---
lasso = Lasso(alpha=0.02)
lasso.fit(X_scaled, scores)

# Select features with non-zero coefficients
nonzero_idx = np.where(lasso.coef_ != 0)[0]
X_selected = X_scaled[:, nonzero_idx]

# --- Cosine similarity ---
cos_sim = cosine_similarity(X_selected)

# For each file, find top_k similar files and predict score
top_k = 5  # change as needed
predicted_scores = []

for i in range(len(df)):
    # sort by similarity (descending), exclude self (i)
    sim_indices = np.argsort(-cos_sim[i])  # descending
    sim_indices = sim_indices[sim_indices != i]  # remove self
    top_indices = sim_indices[:top_k]
    
    # mean score of top_k
    mean_score = scores[top_indices].mean()
    predicted_scores.append(mean_score)

predicted_scores = np.array(predicted_scores)

# --- Compute RMSE ---
rmse = np.sqrt(mean_squared_error(scores, predicted_scores))
print(f"RMSE using top-{top_k} neighbors: {rmse:.4f}")

# --- Store file_name, score, pred in new CSV ---
out_df = pd.DataFrame({
    'file_name': file_names,
    'score': scores,
    'pred': predicted_scores
})
out_df.to_csv('rag_predicted_scores.csv', index=False)
print("Saved predictions to predicted_scores.csv")

# --- Print selected (nonzero coefficient) features ---
feature_names = X.columns
selected_features = feature_names[nonzero_idx]
print("\nFeatures used for similarity (non-zero coefficients):")
print(selected_features.tolist())
