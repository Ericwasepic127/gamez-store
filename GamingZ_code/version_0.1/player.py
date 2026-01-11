import os, subprocess, datetime, json
from tkinter import messagebox as mb
import tkinter as tk

try:
    games = os.listdir('games/')
    g_all = [game.strip('*') for game in games if game.startswith('*') and game.endswith('*')]

    def play(game_dir):
        game_path = f"games/*{game_dir}*/"
        try:
            with open(f"{game_path}config.json", "r") as config:
                conf = json.load(config)
            os.makedirs("logs/", exist_ok=True)
            if conf.get("windowed", True):  
                output = subprocess.run(f"python {game_path}main.py", creationflags=subprocess.CREATE_NO_WINDOW, capture_output=True, text=True)
            else:
                output = subprocess.run(f"python {game_path}main.py", capture_output=True, text=True)
            with open(f"logs/{game_dir}/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt", "w") as log:
                if output.stderr:
                    log.write(output.stderr)
                    mb.showerror("Failed", f"Can't run game! Logs saved in {os.getcwd()}/logs/{game_dir}/")
                elif output.stdout:
                    log.write(output.stdout)
                else:
                    log.write("Code complete")
        except FileNotFoundError:
            mb.showerror("Failed", "Game file not found! ")
        except Exception as e:
            mb.showerror("Error", f"Game error: {e}")

    root = tk.Tk()
    root.title("GameZ player")
    root.geometry("500x300")
    root.resizable(False, False)
    for game in g_all:
        btn = tk.Button(root, text=f"Game: {game}", command=lambda g=game: play(g))
        btn.pack()
    root.mainloop()
except Exception as e:
    mb.showerror("GameZ Crashed", f"Error: {e}")
