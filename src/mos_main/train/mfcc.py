import os
import librosa
import numpy as np
import pandas as pd
from pathlib import Path

# Path to your folder with audio files
PROJECT_ROOT = Path(__file__).resolve().parents[1]
folder_path = PROJECT_ROOT / "analyses" / "voices_converted"

# List to hold features
data = []

# Loop over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith(('.wav')):  # audio file extensions
        file_path = os.path.join(folder_path, file_name)

        # Load audio file
        y, sr = librosa.load(file_path, sr=None)

        # Compute MFCCs (13 coefficients)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

        # Take mean over time (frames) to get one vector per file
        mfccs_mean = np.mean(mfccs, axis=1)  # shape (13,)

        # Append to data list
        data.append([file_name] + mfccs_mean.tolist())

# Create DataFrame
columns = ['filename'] + [f'mfcc_{i+1}' for i in range(13)]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
output_file = "mfcc_features_1000.csv"
df.to_csv(output_file, index=False)

print(f"Saved MFCC features to {output_file}")
