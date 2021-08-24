# create a 3 x 3 grid and fill labels inside it.
import tkinter as tk
window = tk.Tk()

for i in range(0, 3):
    for j in range(0, 3):
        frame = tk.Frame(width = "250", height = "250", borderwidth = 10, relief = tk.RAISED)
        frame.grid(row = i, column = j)
        label = tk.Label(master = frame, text = f"Row {i}, Column {j}")
        label.pack()


window.mainloop()