import pandas as pd

# --- Load both CSV files ---
lasso_csv = 'lasso_predictions.csv'
rag_csv = 'rag_predicted_scores.csv'

df_lasso = pd.read_csv(lasso_csv)
df_rag = pd.read_csv(rag_csv)

# --- Merge on file_name (order-independent) ---
merged_df = pd.merge(
    df_lasso[['file_name', 'pred']], 
    df_rag[['file_name', 'pred']], 
    on='file_name',
    suffixes=('_lasso', '_rag')
)

# Add score column (same in both, we can take from any)
merged_df['score'] = df_lasso.set_index('file_name').loc[merged_df['file_name'], 'score'].values

# Optional: reorder columns
merged_df = merged_df[['file_name', 'score', 'pred_lasso', 'pred_rag']]

# --- Save to CSV ---
merged_df.to_csv('merged_predictions.csv', index=False)
print("Saved merged predictions to merged_predictions.csv")
