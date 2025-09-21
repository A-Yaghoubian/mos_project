from datasets import load_dataset
import soundfile as sf
import numpy as np
import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data_files", default="data/mana_tts/dataset_part_001.parquet")
parser.add_argument("--outdir", default="data/wavs")
parser.add_argument("--max_samples", type=int, default=200)
args = parser.parse_args()

os.makedirs(args.outdir, exist_ok=True)

ds = load_dataset("MahtaFetrat/Mana-TTS", data_files=args.data_files, split="train")
print("Dataset loaded:", len(ds), "rows")

for i, ex in enumerate(ds.select(range(min(len(ds), args.max_samples)))):
    audio = ex["audio"]
    arr, sr = np.array(audio["array"]), audio["sampling_rate"]
    outpath = os.path.join(args.outdir, f"{i}.wav")
    sf.write(outpath, arr, sr)
    if (i+1) % 50 == 0:
        print(f"Saved {i+1} wavs")

print("Done. Saved to", args.outdir)
