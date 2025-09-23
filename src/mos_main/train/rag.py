import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Read CSV file
df = pd.read_csv("mfcc_features.csv")  # Your CSV file from previous step

# Ask user for index of file (row)
index = int(input("Enter the index of the file (row number): "))

# Extract query vector (features 1,3,7,8) from that row
# (remember Python uses 0-based indexing)
selected_features = [1, 3, 7, 8]  # column indices
query_vector = df.iloc[index, selected_features].values.reshape(1, -1)

# Extract all data (only the selected features for each row)
data_matrix = df.iloc[:, selected_features].values

# Compute cosine similarity between query_vector and all rows
similarities = cosine_similarity(query_vector, data_matrix)[0]

# Get top 3 most similar indices (excluding the query itself)
top_indices = np.argsort(similarities)[::-1]  # descending order
top_indices = [i for i in top_indices if i != index][:3]

print("Top 3 similar rows based on features 1,3,7,8:")
for i in top_indices:
    print(f"Index: {i}, Similarity: {similarities[i]:.4f}")
