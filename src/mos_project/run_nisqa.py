import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--wav_dir", default="wavs_converted", help="Directory with wav files")
parser.add_argument("--outdir", default="results", help="Where to save predictions")
args = parser.parse_args()

nisqa_repo = os.path.join("", "NISQA")
weights = os.path.join(nisqa_repo, "weights", "nisqa_tts.tar")

cmd = [
    "python", "run_predict.py",
    "--mode", "predict_dir",
    "--pretrained_model", 'weights/nisqa.tar',
    "--data_dir", args.wav_dir,
    "--num_workers", "0",
    "--bs", "10",
    "--output_dir", args.outdir
]

print("Running NISQA...")
subprocess.run(cmd, cwd=nisqa_repo)
print("Done. Results saved in", args.outdir)
