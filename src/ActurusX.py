
import tkinter as tk

mlbl = "Acturus X"

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=700, bg="black")
canvas.pack()

frame = tk.Frame(root, bg="#2b2b2b")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

label = tk.Label(frame, text=mlbl, bg="#2b2b2b", fg="white")
label.pack()

root.mainloop()
