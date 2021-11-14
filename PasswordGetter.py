import pyperclip
import os
import json

passwordFile = "myPasswords.json"
encPasswordFile = "myPasswords.enc"
if(os.path.exists(passwordFile)):
    key = pyperclip.paste()
    with open(passwordFile,"r") as passwords:
        jsonStr = passwords.read()
    passwordDict = json.loads(jsonStr)
    if(key in passwordDict):
            pyperclip.copy(passwordDict[key])
    else:
        print("Error")

elif(os.path.exists(encPasswordFile)):
    #open password gui so the user can decrypt their passwords
    import PasswordDecrypter
else:
    print("Passwords are corrupted or encrypted")
    exit(0)
