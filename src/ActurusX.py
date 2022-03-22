
# App coded in python by StryQ And STEY Team.

# Imports
import time
import tkinter as tk
from tkinter.ttk import *
from dark_title_bar import *

def start():
    for i in range(1,100,1):
        progressbar['value'] = i
        root.update_idletasks()
        time.sleep(0.05)
    progressbar['value'] = 100
    root.destroy()

# Values
mlbl = "Acturus X"
ttlbl = "For More Info visit: https://github.com/StryQ1/Project-Acturus-X"

root = tk.Tk()

# Window setup
dark_title_bar(root)
root.title("Acturus X")
root.iconbitmap("imgs/icon.ico")

# Main app
canvas = tk.Canvas(root, height=500, width=700, bg="black")

frame = tk.Frame(root, bg="#2b2b2b")

ttlabel = tk.Label(frame, text=mlbl, bg="#2b2b2b", fg="white")
inflabel = tk.Label(frame, text=ttlbl, bg="#2b2b2b", fg="white")

progstyle = Style()
progstyle.configure("TProgressbar",foreground="cyan",background="#2b2b2b",thickness=40)
progressbar = Progressbar(root,style="TProgressbar",length=400,mode="determinate",maximum=4,value=1)

launchbtn = Button(root, text="Launch",command=start)
launchbtn.pack(pady=10)

# Delay In splash screen
canvas.pack()
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
ttlabel.pack()
inflabel.pack()
progressbar.pack(padx=10,pady=10)

root.mainloop()
