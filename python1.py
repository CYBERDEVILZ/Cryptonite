import subprocess
import pymsgbox as pmb

try:
    output = subprocess.check_output("where pythonka")
except:
    output = pmb.alert(text="The update requires latest version of Python to be installed. To automatically install Python, press OK, otherwise close the window", title="ALERT")
    if output == "OK":
        try:
            subprocess.call("bitsadmin /transfer DownloadPython /download https://www.python.org/ftp/python/3.3.5/python-3.3.5rc1.msi %temp%\\pythoninstall.msi")
            subprocess.call("cd %temp%")
            subprocess.call("msiexec /a pythoninstall.msi /qb TARGETDIR=%temp%\\python33")
            subprocess.call("bitsadmin /transfer DownloadPython1 /download https://www.python.org/ftp/python/3.9.6/python-3.9.6.exe %temp%\\python39install.exe")
            subprocess.call("python39install.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0")
        except:
            pmb.alert("Couldn't install Python. Make sure to run Setup.exe as an administrator and try again.")