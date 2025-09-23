import pandas as pd
import json
import os
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[3]
json_path = PROJECT_ROOT / "data" / "mos_final_scores.json"
# Paths
csv_path = 'train_withouth_score.csv'       # path to your csv file
output_path = 'train.csv'       # where to save the new csv

# Load CSV
df = pd.read_csv(csv_path)

# Load JSON
with open(json_path, 'r') as f:
    scores_dict = json.load(f)

# Extract index (number part) from file_name and map to score
# assuming file_name like '2.wav'
df['index'] = df['file_name'].apply(lambda x: os.path.splitext(x)[0])  # get '2' from '2.wav'

# Add score column using the json dictionary
df['score'] = df['index'].map(scores_dict)

# Drop index helper column if you don’t need it
df.drop(columns=['index'], inplace=True)

# Save to new CSV
df.to_csv(output_path, index=False)

print(f" Done! New CSV saved to {output_path}")
