# We are going to play with some widgets here

import tkinter as tk

window = tk.Tk()
# some available widgets

# widget Class          Description
# ---------------------------------
# Label                 display text onto the window
# Button                adds buttons
# Entry                 an entry that allows a single line of text
# Text                  multiline of text
# Frame                 A rectangular region used to group related widgets or provide padding

label = tk.Label(text = "Colourful label boi!", fg = "#ffffff", bg = "#101010", width = "20", height = "10")
label.pack()

button = tk.Button(text = "Clickme", fg = "purple", bg = "white", width = "20", height = "20")
button.pack()

label_for_entry = tk.Label(text = "Enter your name below:- ")
entry = tk.Entry()
entry.insert(0, "You should implement these in classes")
label_for_entry.pack()
entry.pack()
print(entry.get())

# similiarly, one can do for text widget but the only catch is the index. It follows the pattern "<line>.<chars>"

window.mainloop()