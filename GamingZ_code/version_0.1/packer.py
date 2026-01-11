import zipfile
import tkinter as tk
from tkinter import filedialog

def pack_game():
    game_dir = filedialog.askdirectory()
    if game_dir:
        output_file = filedialog.asksaveasfilename(defaultextension=".gzz", filetypes=[("GameZ files", "*.gzz")])
        if output_file:
            with zipfile.ZipFile(output_file, 'w') as zip_ref:
                for root, dirs, files in os.walk(game_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zip_ref.write(file_path, os.path.relpath(file_path, game_dir))
            mb.showinfo("Packed", f"Game packed to {output_file}")

root = tk.Tk()
root.title("GamingZ Packer")

tk.Button(root, text="Pack Game", command=pack_game).pack(pady=20)

root.mainloop()
