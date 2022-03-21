
# App coded in python by StryQ And STEY Team.

# Imports
import tkinter as tk
from dark_title_bar import *

# Values
mlbl = "Acturus X"

root = tk.Tk()

# Window setup
dark_title_bar(root)
root.title("Acturus X")
root.iconbitmap("imgs/icon.ico")

# Main app
canvas = tk.Canvas(root, height=500, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="#2b2b2b")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label = tk.Label(frame, text=mlbl, bg="#2b2b2b", fg="white")
label.pack()

root.mainloop()
