import os
import soundfile as sf
from audiomentations import Compose, AddGaussianNoise, TimeStretch, PitchShift, Shift,AirAbsorption,BandPassFilter,Clip,TimeMask,TimeStretch,Trim
import numpy as np

# Input and output folders
input_folder = "wavs"
output_folder = "wavs_augmented"
os.makedirs(output_folder, exist_ok=True)

# Define augmentation pipeline
augment = Compose([
    #AddGaussianNoise(min_amplitude=0.05, max_amplitude=0.1, p=1),okey p = .3
#     AirAbsorption(
#     min_distance=50.0,
#     max_distance=100.0,
#     p=1.0,
# )No
#BandPassFilter(min_center_freq=100.0, max_center_freq=6000, p=1.0),#okey p= .5
#Clip(a_min = -1, a_max = 1 , p = 1)#okey p = .5
# TimeMask(
#     min_band_part=0.2,
#     max_band_part=0.4,
#     p=1.0,
#)#okey p = .2
# TimeStretch(
#     min_rate=0.5,
#     max_rate=2.0,
#     leave_length_unchanged=True,
#     p=1.0
# )okkey p=.2
# Trim(
#     top_db=40.0,
#     p=1.0
# )NO
    #TimeStretch(min_rate=0.8, max_rate=1.25, p=0.5),
    #PitchShift(min_semitones=-4, max_semitones=4, p=1),okey ,p =  .1
   # Shift(p=0.5),
])

augment = Compose([
   AddGaussianNoise(min_amplitude=0.05, max_amplitude=0.1, p=.3),
   BandPassFilter(min_center_freq=100.0, max_center_freq=6000, p=.5),
   Clip(a_min = -1, a_max = 1 , p = .5),
   TimeMask(
    min_band_part=0.2,
    max_band_part=0.4,
    p=.2,
),
 TimeStretch(
     min_rate=0.5,
     max_rate=2.0,
     leave_length_unchanged=True,
     p=.2
 ),
PitchShift(min_semitones=-4, max_semitones=4, p=.1) 

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
            if len(samples.shape) > 1:
                samples = np.mean(samples, axis=1)

            # Ensure float32 format
            samples = samples.astype(np.float32)

            # Apply augmentations
            augmented_samples = augment(samples=samples, sample_rate=sample_rate)

            # Save augmented file
            sf.write(output_path, augmented_samples, sample_rate)
            print(f" Augmented and saved: {output_path}")

        except Exception as e:
            print(f" Error processing {filename}: {e}")

print("\n All files have been processed and saved to:", output_folder)
