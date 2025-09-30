from datasets import load_dataset
import soundfile as sf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--part", default="dataset/dataset_part_001.parquet", help="Dataset part to download (parquet file)")
parser.add_argument("--outdir", default="data/wavs")
parser.add_argument("--max_samples", type=int, default=200)

args = parser.parse_args()

ds = load_dataset("MahtaFetrat/Mana-TTS", data_files=args.part, split="train")
print("Downloaded partition:", args.part)
print("Rows:", len(ds))
print("Columns:", ds.column_names)

for i, ex in enumerate(ds.select(range(min(len(ds), args.max_samples)))):
    arr = ex["audio"]
    sr = int(ex["samplerate"])
    #print(f'sr:{sr}')
    #arr, sr = np.array(audio["array"]), audio["sampling_rate"]
    outpath = os.path.join(args.outdir, f"{i}.wav")
    sf.write(outpath, arr, sr)
    if (i+1) % 50 == 0:
        print(f"Saved {i+1} wavs")

print("Done. Saved to", args.outdir)
