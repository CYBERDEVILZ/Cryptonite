import requests
import os

file = requests.get("https://www.python.org/ftp/python/3.9.6/python-3.9.6.exe")

with open("python-3.9.6.exe", "wb") as f:
    f.write(file.content)

os.system("python-3.9.6.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0")