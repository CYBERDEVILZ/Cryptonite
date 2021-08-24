# create a window with three frames aligned side by side. Make it responsive

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master = window, height = "100", width = "200", bg = "red")
frame1.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)
frame2 = tk.Frame(master = window, width = 100, bg = "blue")
frame2.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)
frame3 = tk.Frame(master = window, width = 100, bg = "yellow")
frame3.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)

window.mainloop()