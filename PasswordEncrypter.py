import os
from encryptionFunctions import masterPasswordCheck
from encryptionFunctions import encryptPasswords
SRCFILESTRING = "myPasswords.json"
DESFILESTRING = "myPasswords.enc"
if(os.path.exists(SRCFILESTRING) and os.path.exists(DESFILESTRING)):
    print("You have not started the PasswordStartup.exe or your files are corrupted")
    exit(-1)
if(os.path.exists(DESFILESTRING)):
    print("Passwords already encrypted")
    exit(-1)
if(os.path.exists(SRCFILESTRING)):
    if(not os.path.exists(r"hash.txt")):
        print("You have not started the PasswordStartup.exe or your files are corrupted")
    #Check to make sure the password is correct using the one way hash sha256
    myPassword = masterPasswordCheck()
    encryptPasswords(SRCFILESTRING, DESFILESTRING, myPassword)
    os.remove(SRCFILESTRING)
else:
    print("You have not started the PasswordStartup.exe or your files are corrupted")