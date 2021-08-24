# create a text editor using tkinter

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filename = askopenfilename(filetypes = filetypes)
    if not filename:
        return
    with open (filename, "r") as f:
        text = f.read()
        entry_text.delete("1.0", tk.END)
        entry_text.insert("1.0", text)
        window.title(f"Editing -  {filename}")

def save_file():
    filename = asksaveasfilename(filetypes = filetypes)
    if not filename:
        return
    with open(filename, "w") as f:
        edited_text = entry_text.get("1.0", tk.END)
        f.write(edited_text)

filetypes = [("All Files", "*.*"), ("Text Files", "*.txt")] # file select drop down menu

window = tk.Tk()
window.title("Text Editor")                                 # given title to window

window.rowconfigure(0, weight = 1, minsize = 800)           # responsive 1st row
window.columnconfigure(1, weight = 1, minsize = 800)        # responsive 2nd column

menu_frame = tk.Frame(window)
menu_frame.grid(row = 0, column = 0, sticky = "ns")

btn_open = tk.Button(master = menu_frame, text = "Open File", borderwidth = 1, command = open_file)
btn_open.grid(row = 0, column = 0, sticky = "ew", padx = 5, pady = 5)
btn_save = tk.Button(master = menu_frame, text = "Save File as...", borderwidth = 1, command = save_file)
btn_save.grid(row = 1, column = 0, sticky = "ew", padx = 5, pady = 3)

entry_text = tk.Text(master = window)
entry_text.grid(row = 0, column = 1, sticky = "nsew")


window.mainloop()
