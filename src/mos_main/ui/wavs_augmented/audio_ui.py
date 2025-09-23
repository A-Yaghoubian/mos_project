import tkinter as tk
from tkinter import messagebox
import pygame
import json
# Initialize pygame mixer
pygame.mixer.init()

# --- Global state ---
MUSIC_FILE_INDEX = 0  # <-- replace with your file path
player_number = None     # store selected player number
score_json = [{},{},{},{}]
play_list_player_1 = [i for i in range(200) if i % 6 in (1, 3, 5)]
play_list_player_2 = [i for i in range(200) if i % 6 in (0, 1, 4)]
play_list_player_3 = [i for i in range(200) if i % 6 in (0, 2, 3)]
play_list_player_4 = [i for i in range(200) if i % 6 in (2, 4, 5)]
player_list = None


def save_to_file(json_data):
    with open("data.json", "w") as f:
        json.dump(json_data, f, indent=4)  # indent=4 makes it pretty-printed
# --- Page 2: Music Player UI ---
def open_music_player(root):
    # Clear previous widgets
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Simple Music Player")
    root.geometry("300x300")

    def play_music():
        try:
            MUSIC_FILE = f"{player_list[MUSIC_FILE_INDEX]}.wav"
            pygame.mixer.music.load(MUSIC_FILE)
            pygame.mixer.music.play()
        except Exception as e:
            messagebox.showerror("Error", f"Could not play file: {e}")

    def next_music():
        global MUSIC_FILE_INDEX,player_list
        try:
            if MUSIC_FILE_INDEX < len(player_list) - 1:
                MUSIC_FILE_INDEX += 1
        except Exception as e:
            messagebox.showerror("Error", f"Could not play file: {e}")

    def show_score():
        global score_json
        score = score_var.get()
        score_json[player_number - 1 ][str(player_list[MUSIC_FILE_INDEX])] = score
        save_to_file(score_json)
        messagebox.showinfo("Score", f"Player {player_number} gave a score of {score}/5")

    # Buttons
    play_btn = tk.Button(root, text="▶ Play", command=play_music, width=12, height=2)
    next_btn = tk.Button(root, text="Next ▶", command=next_music, width=12, height=2)

    play_btn.pack(pady=5)
    next_btn.pack(pady=5)

    # --- Score Section (Radio Buttons 1–5) ---
    score_var = tk.IntVar(value=0)  # Default score is 0 (not selected)

    score_frame = tk.LabelFrame(root, text="Rate the song (1-5)", padx=10, pady=10)
    score_frame.pack(pady=10)

    for i in range(1, 6):
        tk.Radiobutton(score_frame, text=str(i), variable=score_var, value=i).pack(side="left")

    submit_btn = tk.Button(root, text="Submit Score", command=show_score, width=12)
    submit_btn.pack(pady=5)


# --- Page 1: Player Selection ---
def open_player_selection(root):
    root.title("Player Selection")
    root.geometry("300x200")

    player_var = tk.IntVar(value=0)

    label = tk.Label(root, text="Select Player Number:", font=("Arial", 12))
    label.pack(pady=10)

    for i in range(1, 5):
        tk.Radiobutton(root, text=f"Player {i}", variable=player_var, value=i).pack(anchor="w")

    def start_game():
        global player_number,player_list
        player_number = player_var.get()
        if player_number == 1:
            player_list = play_list_player_1
        elif player_number == 2:
            player_list = play_list_player_2
        elif player_number == 3:
            player_list = play_list_player_2
        elif player_number == 4:
            player_list = play_list_player_4
        if player_number == 0:
            messagebox.showwarning("Warning", "Please select a player number first!")
        else:
            open_music_player(root)

    start_btn = tk.Button(root, text="Start ▶", command=start_game, width=12, height=2)
    start_btn.pack(pady=15)


# --- Main App ---
root = tk.Tk()
open_player_selection(root)
root.mainloop()
