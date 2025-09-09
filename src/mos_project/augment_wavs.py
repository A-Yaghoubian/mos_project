import os
import glob
import argparse
import numpy as np
import soundfile as sf
import librosa
import random

parser = argparse.ArgumentParser()
parser.add_argument("--indir", default="data/wavs", help="Folder with original wavs")
parser.add_argument("--outdir", default="data/augmented_wavs", help="Where to save augmented wavs")
parser.add_argument("--max_samples", type=int, default=200, help="How many wavs to process")
args = parser.parse_args()

os.makedirs(args.outdir, exist_ok=True)

def augment_pitch_shift(y, sr):
    steps = random.choice([-2, -1, 1, 2])  # semitones
    return librosa.effects.pitch_shift(y, sr, n_steps=steps)

def augment_time_stretch(y):
    rate = random.uniform(0.8, 1.2)  # slower/faster
    return librosa.effects.time_stretch(y, rate)

def augment_add_noise(y):
    noise = np.random.normal(0, 0.005, y.shape)
    return y + noise

def augment_volume(y):
    gain = random.uniform(0.5, 1.5)
    return y * gain

augmentations = {
    "pitch": augment_pitch_shift,
    "stretch": augment_time_stretch,
    "noise": augment_add_noise,
    "volume": augment_volume,
}

# Select wav files
wav_files = sorted(glob.glob(os.path.join(args.indir, "*.wav")))[: args.max_samples]

print(f"Found {len(wav_files)} wavs. Applying augmentations...")

for wav_path in wav_files:
    y, sr = librosa.load(wav_path, sr=None)
    base = os.path.splitext(os.path.basename(wav_path))[0]

    for name, func in augmentations.items():
        try:
            y_aug = func(y.copy(), sr) if "sr" in func.__code__.co_varnames else func(y.copy())
            outpath = os.path.join(args.outdir, f"{base}_{name}.wav")
            sf.write(outpath, y_aug, sr)
        except Exception as e:
            print(f"⚠️ Skipping {name} for {wav_path}: {e}")

print("✅ Augmentation finished. Saved to:", args.outdir)
