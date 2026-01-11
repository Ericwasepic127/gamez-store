import os, subprocess, zipfile, tkinter as tk
from tkinter import messagebox as mb
import tkinter.filedialog
import shutil
import json

def install_game():
    game_file = tk.filedialog.askopenfilename(filetypes=[("GameZ files", "*.gzz")])
    if game_file:
        try:
            game_name = os.path.basename(game_file).replace('.gzz', '')
            extract_path = f"games/{game_name}"
            with zipfile.ZipFile(game_file, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            with open(f"{extract_path}/config.json", "r") as config:
                conf = json.load(config)
            mb.showinfo("Installed", f"{game_name} installed!")
            if mb.askyesno('Launch Game', f'Installed {game_name} successfully. Launch now?'):
                if conf.get("windowed", True):  
                    subprocess.run(f"python {extract_path}/main.py", creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    subprocess.run(f"python {extract_path}/main.py")
        except Exception as e:
            mb.showerror("Error", f"Install failed: {e}")

def delete_game():
    game_path = tk.filedialog.askdirectory(initialdir="games/")
    if game_path:
        confirm = mb.askyesno("Delete Game", f"Delete {game_path}?")
        if confirm:
            try:
                shutil.rmtree(game_path)
                mb.showinfo("Deleted", f"Removed {game_path}")
            except Exception as e:
                mb.showerror("Error", f"Can't delete: {e}")

root = tk.Tk()
root.title("GameZ Manager")
root.geometry("300x200")

tk.Button(root, text="Install Game", command=install_game).pack(pady=20)
tk.Button(root, text="Delete Game", command=delete_game).pack(pady=20)

root.mainloop()
