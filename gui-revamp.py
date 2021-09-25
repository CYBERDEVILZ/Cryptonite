import tkinter as tk
import tkinter.ttk as ttk

def clear():
    pass

def clear1(*args):
    pass

def key_collect():
    pass

window = tk.Tk()
window.title("Cryptonite")
window.resizable(0,0)
window.rowconfigure(0, minsize = 700)
window.columnconfigure(0, minsize = 1000)
window.columnconfigure(1, minsize = 300)

style = ttk.Style()
style.configure('TButton', font=("Apple Chancery", 18))
style.configure('small.TButton', font=("Apple Chancery", 8))

frm_main = tk.Frame(master = window, bg = "black")
frm_main.grid(row = 0, column = 0, sticky = "nsew", padx = 2, pady = 2)

frm_main.rowconfigure([0,1,2,3,4,5,6,7], weight = 1)
frm_main.columnconfigure(0, weight = 1)
frm_main.columnconfigure(1, weight = 1)

lbl_main = tk.Label(master = frm_main, text = "WARNING!", font=("Apple Chancery", 50), fg = "red", bg = "black")
lbl_main.grid(row = 0, column = 0, pady = 5, columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = "Some / All of Your Files Have Been Encrypted!", font=("Apple Chancery", 40), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 1, column = 0, columnspan = 2)
decryption_key = tk.Entry(master = frm_main, font=("Apple Chancery", 25), relief = tk.SUNKEN, borderwidth = 3, fg = "grey")
decryption_key.grid(row = 2, column = 0, columnspan = 1, sticky = "e")
decryption_key.insert("0", "DECRYPTION_KEY")
decryption_key.bind("<Button-1>", clear1)
decryption_key_button = ttk.Button(style = 'TButton', master = frm_main, text = "Submit", command = key_collect)
decryption_key_button.grid(row = 2, column = 1, sticky = "w", padx = 5)
lbl_main1 = tk.Label(master = frm_main, text = "It uses military grade encryption to encrypt your files. It requires a DECRYPTION_KEY for decryption process.\nIf you think its a joke, try opening up your files from the file viewer on the right hand side of this frame.", font=("Apple Chancery", 15), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 3, column = 0, columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = "Do not Close this Window! Else face the consequences!", font=("Apple Chancery", 25), bg = "black", fg = "red")
lbl_main1.grid(row = 4, column = 0, columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = "What you can do?", font=("Apple Chancery", 20), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 5, column = 0, columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = "Don't worry! Your files can still be decrypted.\nYou just need to put in the correct DECRYPTION_KEY in the text box provided.\n\nIn order to get the DECRYPTION_KEY, 1. Send us the specified amount of BTC to the address mentioned below. 2. Send us the\nvalid screenshots via email along with your UNIQUE_ID. Do that and we will provide the correct DECRYPTION_KEY via mail.\n\nRemember! You will have only ONE CHANCE to enter the DECRYPTION_KEY.\n\nSo, do not try to be a Smart Alec.", font=("Apple Chancery", 15), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 6, column = 0, columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = f"BTC AMOUNT: \tBTC WALLET: \tEMAIL: \t", font=("Apple Chancery", 10), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 7, column = 0, sticky = "w", columnspan = 2)
lbl_main1 = tk.Label(master = frm_main, text = f"UNIQUE_ID: ", font=("Apple Chancery", 10), bg = "black", fg = "#39ff14")
lbl_main1.grid(row = 7, column = 0, sticky = "e", columnspan = 2)

frm_editor = tk.Frame(bg = "black", master = window)
frm_editor.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

frm_editor.rowconfigure(0, minsize = 20, weight = 0)
frm_editor.columnconfigure(0, minsize = 0, weight = 1)
frm_editor.rowconfigure(1, minsize = 600, weight = 1)


btn_editor = ttk.Button(master = frm_editor, text = "Open File", style = "small.TButton")
btn_editor.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "e")

btn_editor1 = ttk.Button(master = frm_editor, text = "Clear Screen", command = clear, style = "small.TButton")
btn_editor1.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = "ns")

txt_editor = tk.Text(master = frm_editor)
txt_editor.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)
txt_editor.insert("3.0", "Open file that ends with .cryptn8 extension and see it is encrypted.")

window.mainloop()