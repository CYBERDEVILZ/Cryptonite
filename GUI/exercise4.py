# print keyboard events.

import tkinter as tk
window = tk.Tk()

def event_handle(event):
    print(event.char)

window.bind("<Key>", event_handle)

window.mainloop()