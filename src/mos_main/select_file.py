import os
import random
import shutil

def random_select_files(folder_path, output_path, threshold=0.1, move=False):
    """
    Randomly select files based on threshold and copy/move them to another folder.

    Args:
        folder_path (str): Path to the folder containing files.
        output_path (str): Destination folder for selected files.
        threshold (float): Probability of selecting a file (default=0.1 → 10%).
        move (bool): If True, move instead of copy.
    """
    os.makedirs(output_path, exist_ok=True)

    for f in os.listdir(folder_path):
        file_path = os.path.join(folder_path, f)
        if os.path.isfile(file_path):
            if random.random() < threshold:  # random number in [0,1)
                if move:
                    shutil.move(file_path, os.path.join(output_path, f))
                else:
                    shutil.copy(file_path, os.path.join(output_path, f))
                print(f"Selected: {f}")

# Example usage:
# Copy ~10% of files
random_select_files(r'E:\vcc_2018\vcc_2018', r"E:\vcc_2018\selected", threshold=0.1, move=False)
