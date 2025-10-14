import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
<<<<<<< HEAD
parser.add_argument("--wav_dir", default="C:/Users/Moein/Desktop/speech/wavs_augmented", help="Directory with wav files")
parser.add_argument("--outdir", default="C:/Users/Moein/Desktop/speech/wavs_augmented", help="Where to save predictions")
=======
parser.add_argument("--wav_dir", default="./data/nisqa_vcc_mos_2018/200_selected", help="Directory with wav files")
parser.add_argument("--outdir", default="./data/nisqa_vcc_mos_2018/results", help="Where to save predictions")
>>>>>>> f21af0e929374d7f659b86816b3725c8e7c12115
args = parser.parse_args()

nisqa_repo = os.path.join("", "NISQA")
weights = os.path.join(nisqa_repo, "weights", "nisqa_tts.tar")

cmd = [
    "python", "run_predict.py",
    "--mode", "predict_dir",
    "--pretrained_model", 'weights/nisqa.tar',
    "--data_dir", os.path.abspath(args.wav_dir),
    "--num_workers", "0",
    "--bs", "10",
    "--output_dir", os.path.abspath(args.outdir)
]

print("Running NISQA...")
subprocess.run(cmd, cwd=nisqa_repo)
print("Done. Results saved in", args.outdir)
