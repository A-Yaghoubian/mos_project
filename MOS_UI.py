import tkinter as tk
from tkinter import filedialog
import pygame
import os
import time
import threading

pygame.mixer.init()

root = tk.Tk()
root.title("Music Player")
root.geometry("400x250")

# Playlist
playlist = []
current_index = 0

# Progress bar
progress = tk.Scale(root, from_=0, to=100, orient="horizontal", length=300)
progress.pack(pady=20)

def load_music_folder():
    global playlist, current_index
    folder = filedialog.askdirectory()
    if folder:
        playlist = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp3")]
        playlist.sort()
        current_index = 0
        play_music()

def play_music():
    global current_index
    if playlist:
        pygame.mixer.music.load(playlist[current_index])
        pygame.mixer.music.play()

def next_music():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        play_music()

def prev_music():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        play_music()

def update_progress():
    while True:
        if pygame.mixer.music.get_busy():
            pos = pygame.mixer.music.get_pos() // 1000
            progress.set(pos)
        time.sleep(1)

# Buttons
prev_button = tk.Button(root, text="Previous", command=prev_music)
play_button = tk.Button(root, text="Play", command=play_music)
next_button = tk.Button(root, text="Next", command=next_music)
load_button = tk.Button(root, text="Load Folder", command=load_music_folder)

load_button.pack(pady=5)
prev_button.pack(side="left", padx=20)
play_button.pack(side="left", padx=20)
next_button.pack(side="left", padx=20)

# Start progress bar updater thread
threading.Thread(target=update_progress, daemon=True).start()

root.mainloop()
