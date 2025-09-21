import os
import librosa
import soundfile as sf

input_folder = 'wavs'
output_folder = 'wavs_converted'

target_sr = 48000  # target sample rate

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for i in range(200):
    input_path = os.path.join(input_folder, f'{i}.wav')
    output_path = os.path.join(output_folder, f'{i}.wav')
    
    try:
        # Load audio with librosa (resamples to target_sr automatically)
        audio, sr = librosa.load(input_path, sr=target_sr, mono=False)  # keep stereo if exists

        # Save audio with soundfile
        sf.write(output_path, audio.T if audio.ndim > 1 else audio, target_sr)
        print(f'{i}.wav converted successfully')
    
    except Exception as e:
        print(f'Error converting {i}.wav: {e}')
