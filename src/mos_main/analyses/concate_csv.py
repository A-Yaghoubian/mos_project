import pandas as pd

def merge_csv(file_a, file_b, output_file):
    # Load CSVs
    df_a = pd.read_csv(file_a)
    df_b = pd.read_csv(file_b)

    # Create a helper column in A to match B's "filepath_deg"
    df_a["filepath_deg"] = "VCC_2018/" + df_a["deg"].astype(str)

    # Merge on this relation
    merged_df = pd.merge(df_a, df_b, on="filepath_deg", how="inner")

    # Save result to new CSV
    merged_df.to_csv(output_file, index=False)

    print(f"Merged file saved to {output_file}")

# Example usage:
merge_csv("nisqa_results_1000_converted.csv", "english_1000_selected.csv", "merged_english_1000_converted_voices.csv")
