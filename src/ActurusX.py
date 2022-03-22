
# App coded in python by StryQ And STEY Team.

# Imports
import time
import tkinter as tk
from tkinter.ttk import *
from dark_title_bar import *

def start():
    load = 100
    x = 0
    speed = 1
    while(x<task):
        time.sleep(0.05)
        bar ['value']+=(speed/load)*100
        x+=speed
        window.update_idletasks()

# Values
mlbl = "Acturus X"

root = tk.Tk()

# Window setup
dark_title_bar(root)
root.title("Acturus X")
root.iconbitmap("imgs/icon.ico")

# Progressbar
bar = Progressbar(root, orient=HORIZONTAL, lenght=350)
bar.pack(pady=10)

# Main app
canvas = tk.Canvas(root, height=500, width=700, bg="black")

frame = tk.Frame(root, bg="#2b2b2b")

label = tk.Label(frame, text=mlbl, bg="#2b2b2b", fg="white")

# Delay In splash screen
time.sleep(5.5)
bar.delete()
canvas.pack()
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
label.pack()

root.mainloop()
