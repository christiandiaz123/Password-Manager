import os
from encryptionFunctions import masterPasswordCheck
from encryptionFunctions import decryptPasswords
SRCFILESTRING = "myPasswords.enc"
DESFILESTRING = "myPasswords.json"
if(os.path.exists("myPasswords.json") and os.path.exists(SRCFILESTRING)):
    print("You have not started the PasswordStartup.exe or your files are corrupted")
    exit(-1)
if(os.path.exists("myPasswords.json")):
    print("Passwords already decrypted")
    exit(-1)
if(os.path.exists(SRCFILESTRING)):
    if(not os.path.exists(r"hash.txt")):
        print("You have not started the PasswordStartup.exe or your files are corrupted")
    #Check to make sure the password is correct using the one way hash sha256
    myPassword = masterPasswordCheck()
    decryptPasswords(SRCFILESTRING,DESFILESTRING,"nonce.binary", myPassword)
    os.remove(SRCFILESTRING)
else:
    print("You have not started the PasswordStartup.exe or your files are corrupted")






#encrypter = AES.new(myPaddedPassword, AES.MODE_GCM, nonce=nonce)
#decLine = encrypter.decrypt(encLine)
#print(decLine.decode("utf-8"))