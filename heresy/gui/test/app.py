import tkinter as tk

root = tk.Tk()

# --- CREATE ELEMENT ---
myLabel = tk.Label(root, text="Hello World")

# --- ADD TO UI ---
myLabel.pack()

root.mainloop()
