import os
import glob
import argparse
import numpy as np
import soundfile as sf
from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, Shift

parser = argparse.ArgumentParser()
parser.add_argument("--indir", default="data/wavs", help="Folder with original wavs")
parser.add_argument("--outdir", default="data/augmented_wavs_audiomentations", help="Where to save augmented wavs")
parser.add_argument("--max_samples", type=int, default=200, help="How many wavs to process")
args = parser.parse_args()

os.makedirs(args.outdir, exist_ok=True)

# Define augmentation pipeline
augment = Compose([
    AddGaussianNoise(min_amplitude=0.001, max_amplitude=0.015, p=0.5),
    TimeStretch(min_rate=0.8, max_rate=1.25, p=0.5),
    PitchShift(min_semitones=-4, max_semitones=4, p=0.5),
    Shift(min_fraction=-0.5, max_fraction=0.5, p=0.5),
])

# Collect wav files
wav_files = sorted(glob.glob(os.path.join(args.indir, "*.wav")))[: args.max_samples]
print(f"Found {len(wav_files)} wavs. Applying audiomentations...")

for wav_path in wav_files:
    samples, sr = sf.read(wav_path)
    # Ensure float32 (audiomentations requirement)
    if samples.dtype != np.float32:
        samples = samples.astype(np.float32)

    augmented_samples = augment(samples=samples, sample_rate=sr)

    base = os.path.splitext(os.path.basename(wav_path))[0]
    outpath = os.path.join(args.outdir, f"{base}_aug.wav")
    sf.write(outpath, augmented_samples, sr)

print("✅ Audiomentations finished. Saved to:", args.outdir)
