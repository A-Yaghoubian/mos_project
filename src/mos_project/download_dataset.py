from datasets import load_dataset
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--part", default="dataset/dataset_part_001.parquet", help="Dataset part to download (parquet file)")
parser.add_argument("--outdir", default="data/mana_tts", help="Where to save parquet")
args = parser.parse_args()

ds = load_dataset("MahtaFetrat/Mana-TTS", data_files=args.part, split="train")
print("Downloaded partition:", args.part)
print("Rows:", len(ds))
print("Columns:", ds.column_names)
# Save dataset locally
ds.save_to_disk(args.outdir)