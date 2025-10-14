import os
import librosa
import pandas as pd
import soundfile as sf

csv_path = r"E:\VCC_2018.csv"  # Original CSV file
audio_folder = r"E:\VCC_2018\VCC_2018"  # Original audio folder
output_folder = "./"   # Output folder
output_csv = "english_1000_selected.csv"  # Output CSV file

os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv(csv_path)
seed = 8
df_selected = df.sample(n=1000, random_state=seed)

# Loop through and save audios with 48000 sample rate
for idx, row in df_selected.iterrows():
    filename = row["filepath_deg"]
    filename = filename.split('/')[-1]
    filepath = os.path.join(audio_folder, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
    
    # Read audio and resample if needed
    data, sr = sf.read(filepath)
    if sr != 48000:
        data = librosa.resample(data.T, orig_sr=sr, target_sr=48000).T
        sr = 48000
    
    # Save file to new folder
    out_path = os.path.join(output_folder, filename)
    sf.write(out_path, data, sr)
    
# Save new CSV
df_selected.to_csv(output_csv, index=False)

print("Successfully selected and saved 200 files.")