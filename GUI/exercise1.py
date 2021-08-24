# create a window, add an entry widget and take some text inside it.

import tkinter as tk
window = tk.Tk()


frame = tk.Frame()
frame.pack(side=tk.LEFT)

lbl_entry = tk.Label(master=frame, text="Enter the text: ")
lbl_entry.pack()

frame = tk.Frame()
frame.pack(side=tk.LEFT)

ent_get = tk.Entry(master=frame)
ent_get.pack()

window.mainloop()