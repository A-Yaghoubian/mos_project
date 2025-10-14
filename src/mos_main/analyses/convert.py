import os
from pydub import AudioSegment

# === CONFIGURATION ===
input_folder = "voices"       # Folder with original files
output_folder = "voices_converted"     # Folder to save 48kHz files
target_rate = 48000                # Target sampling rate (Hz)

# === CREATE OUTPUT FOLDER IF NOT EXIST ===
os.makedirs(output_folder, exist_ok=True)

# === PROCESS FILES ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".wav", ".mp3", ".flac", ".ogg", ".m4a")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Load and convert
        audio = AudioSegment.from_file(input_path)
        audio = audio.set_frame_rate(target_rate)

        # Export with same format
        audio.export(output_path, format=filename.split('.')[-1])

        print(f"Converted: {filename} → {output_path}")

print(" All files converted to 48kHz successfully!")
