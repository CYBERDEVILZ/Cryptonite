import tkinter as tk

window =  tk.Tk()                                           # creates a an instance of Tk() class (pops up a responsive window)

greeting = tk.Label(text="Hello there, Welcome to tkinter") # creates a label
greeting.pack()                                             # adds it to the window


window.mainloop()                                           # runs the event loop and it listens for events.