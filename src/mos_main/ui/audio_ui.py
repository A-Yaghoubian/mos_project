# Import libraries
import tkinter as tk
from tkinter import messagebox
import pygame
import json
import os
from pathlib import Path

# Initialize pygame mixer
pygame.mixer.init()

# --- Global state ---
MUSIC_FILE_INDEX = 0            # index in the current player's playlist
player_number = None            # store selected player number
score_json = [{}, {}, {}, {}]   # one dict per player
play_list_player_1 = [i for i in range(200) if i % 6 in (1, 3, 5)]
play_list_player_2 = [i for i in range(200) if i % 6 in (0, 1, 4)]
play_list_player_3 = [i for i in range(200) if i % 6 in (0, 2, 3)]
play_list_player_4 = [i for i in range(200) if i % 6 in (2, 4, 5)]
player_list = None

PROJECT_ROOT = Path(__file__).resolve().parents[3]
AUDIO_DIR = PROJECT_ROOT / "data" / "wavs_augmented"   # mos_project/data/wavs_augmented
DATA_FILE  = PROJECT_ROOT / "data" / "mos_scores.json" # mos_project/data/mos_scores.json


# --- Load & Save ---
def load_from_file():
    global score_json
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            # sanity: must be 4 dicts
            if isinstance(data, list) and len(data) == 4 and all(isinstance(x, dict) for x in data):
                score_json = data
        except Exception:
            pass

def save_to_file(json_data):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)  # ensure mos_project/data exists
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4)


# --- Music Player UI ---
def open_music_player(root):
    global MUSIC_FILE_INDEX
    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    load_from_file()  # load previous scores if exist
    MUSIC_FILE_INDEX = 0

    root.title("Simple Music Player")
    root.geometry("800x500+1200+600")

    # --- helpers ---
    def current_file_basename():
        return f"{player_list[MUSIC_FILE_INDEX]}"

    def current_file_path():
        base = f"{player_list[MUSIC_FILE_INDEX]}"
        # Prefer .wav, but fall back to .wavs if that’s what you have
        for ext in (".wav", ".wavs"):
            cand = AUDIO_DIR / f"{base}{ext}"
            if cand.exists():
                return str(cand)
        raise FileNotFoundError(f"Audio not found for {base} (.wav/.wavs) in {AUDIO_DIR}")

    def play_music():
        try:
            MUSIC_FILE = current_file_path()
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Could not play file: {e}")

    def stop_music():
        try:
            pygame.mixer.music.stop()
        except Exception:
            pass

    def update_ui():
        # Update labels and set radio to existing score if present
        file_label_var.set(f"File: {current_file_basename()}  ({MUSIC_FILE_INDEX+1}/{len(player_list)})")
        # read stored score if any
        existing = score_json[player_number - 1].get(str(player_list[MUSIC_FILE_INDEX]))
        score_var.set(int(existing) if existing is not None else 0)

    def next_music():
        nonlocal_btn_guard = True
        stop_music()
        global MUSIC_FILE_INDEX
        if MUSIC_FILE_INDEX < len(player_list) - 1:
            MUSIC_FILE_INDEX += 1
            update_ui()
        else:
            messagebox.showinfo("End", "You reached the last file.")
        # (optional) auto-play the selected file:
        # play_music()

    def prev_music():
        stop_music()
        global MUSIC_FILE_INDEX
        if MUSIC_FILE_INDEX > 0:
            MUSIC_FILE_INDEX -= 1
            update_ui()
        else:
            messagebox.showinfo("Start", "You are at the first file.")
        # (optional) auto-play:
        # play_music()

    def show_score():
        global score_json
        score = score_var.get()
        if score not in (1, 2, 3, 4, 5):
            messagebox.showwarning("No score", "Please select a score (1–5) before submitting.")
            return
        # store/overwrite score
        score_json[player_number - 1][str(player_list[MUSIC_FILE_INDEX])] = score
        save_to_file(score_json)
        messagebox.showinfo("Saved", f"Saved: Player {player_number} scored {score}/5 for {current_file_path()}")

    def back_to_selection():
        stop_music()
        open_player_selection(root)

    # --- UI ---
    header = tk.Label(root, text=f"Player {player_number} – MOS Rating", font=("Arial", 14, "bold"))
    header.pack(pady=8)

    file_label_var = tk.StringVar()
    file_label = tk.Label(root, textvariable=file_label_var, font=("Arial", 11))
    file_label.pack(pady=4)

    # Transport controls
    controls = tk.Frame(root)
    controls.pack(pady=8)

    prev_btn = tk.Button(controls, text="◀ Previous", command=prev_music, width=12, height=2)
    play_btn = tk.Button(controls, text="▶ Play", command=play_music, width=12, height=2)
    next_btn = tk.Button(controls, text="Next ▶", command=next_music, width=12, height=2)

    prev_btn.grid(row=0, column=0, padx=4)
    play_btn.grid(row=0, column=1, padx=4)
    next_btn.grid(row=0, column=2, padx=4)

    # --- Score Section (Radio Buttons 1–5) ---
    score_var = tk.IntVar(value=0)  # 0 means not selected
    score_frame = tk.LabelFrame(root, text="Rate the audio (1 = bad, 5 = excellent)", padx=10, pady=10)
    score_frame.pack(pady=10)

    for i in range(1, 6):
        tk.Radiobutton(score_frame, text=str(i), variable=score_var, value=i).pack(side="left", padx=4)

    submit_btn = tk.Button(root, text="Submit Score", command=show_score, width=14)
    submit_btn.pack(pady=6)

    # Navigation back to selection screen
    back_screen_btn = tk.Button(root, text="⬅ Back to Player Select", command=back_to_selection)
    back_screen_btn.pack(pady=6)

    # initialize UI
    update_ui()


# --- Player Selection ---
def open_player_selection(root):
    # Clear and set up
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Player Selection")
    root.geometry("500x300+1200+600")

    player_var = tk.IntVar(value=0)

    label = tk.Label(root, text="Select Player Number:", font=("Arial", 12))
    label.pack(pady=10)

    for i in range(1, 5):
        tk.Radiobutton(root, text=f"Player {i}", variable=player_var, value=i).pack(anchor="w")

    def start_game():
        global player_number, player_list
        player_number = player_var.get()
        if player_number == 0:
            messagebox.showwarning("Warning", "Please select a player number first!")
            return

        # assign playlist
        if player_number == 1:
            player_list = play_list_player_1
        elif player_number == 2:
            player_list = play_list_player_2
        elif player_number == 3:
            player_list = play_list_player_3  # FIXED: was player_2
        elif player_number == 4:
            player_list = play_list_player_4

        open_music_player(root)

    start_btn = tk.Button(root, text="Start ▶", command=start_game, width=12, height=2)
    start_btn.pack(pady=15)

    # Optional exit button as a "back" for this state
    quit_btn = tk.Button(root, text="Exit", command=root.destroy)
    quit_btn.pack(pady=4)


# --- Main App ---
root = tk.Tk()
open_player_selection(root)
root.mainloop()
