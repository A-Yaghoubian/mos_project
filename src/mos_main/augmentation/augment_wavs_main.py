import os
import soundfile as sf
from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, BandPassFilter, Clip
import numpy as np

# Input and output folders
input_folder = "./data/wavs_converted"
output_folder = "./data/wavs_augmented_2"
os.makedirs(output_folder, exist_ok=True)

# target RMS energy level
TARGET_RMS = 0.1

def normalize_energy(samples, target_rms=TARGET_RMS):
    rms = np.sqrt(np.mean(samples**2))
    if rms > 0:
        samples = samples * (target_rms / rms)

    return samples

# Define augmentation pipeline
augment = Compose([
    AddGaussianNoise(min_amplitude=0.05, max_amplitude=0.1, p=.3),
    BandPassFilter(min_center_freq=100.0, max_center_freq=6000, p=.5),
    Clip(a_min=-1, a_max=1, p=.5),
    TimeStretch(min_rate=0.2, max_rate=6, leave_length_unchanged=True, p=.3),
    PitchShift(min_semitones=-4, max_semitones=4, p=.3)
])

# Process each wav file
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Load audio file
            samples, sample_rate = sf.read(input_path)

            # Convert stereo to mono if needed
            if samples.ndim > 1:
                samples = np.mean(samples, axis=1)

            # Skip empty files
            if len(samples) == 0:
                print(f" Skipped empty file: {filename}")
                continue

            # Ensure float32 format
            samples = samples.astype(np.float32)

            # Apply augmentations
            augmented_samples = augment(samples=samples, sample_rate=sample_rate)

            # normalize energy
            augmented_samples = normalize_energy(augmented_samples)
            
            # Save augmented file
            sf.write(output_path, augmented_samples, sample_rate)
            print(f" Augmented and saved: {output_path}")

        except Exception as e:
            print(f" Error processing {filename}: {e}")

print("\n All files have been processed and saved to:", output_folder)
