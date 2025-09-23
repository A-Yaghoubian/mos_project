import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
input_file = PROJECT_ROOT / "data" / "mos_scores.json"
output_file = PROJECT_ROOT / "data" / "mos_final_scores.json"
# Load JSON from file
with open(input_file, "r") as f:
    data = json.load(f)

# Calculate mean for each index
means = {}
for d in data:
    for key, value in d.items():
        key = str(key)  # Keep as string for JSON compatibility
        if key not in means:
            means[key] = []
        means[key].append(value)

# Compute final mean
mean_result = {k: sum(v)/len(v) for k, v in means.items()}

# Save result to new JSON file
with open(output_file, "w") as f:
    json.dump(mean_result, f, indent=4)

print("Mean values saved to 'mean_result.json'")
