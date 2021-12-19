def masterPasswordCheck():
    with open('hash.txt', 'r') as hashFile:
        hashVal = hashFile.read()
    while(True):
        from hashlib import sha256
        myPassword = input("Please input your Master Password:").encode("utf-8")
        if(sha256(myPassword).hexdigest()==hashVal):
            return myPassword
        else:
            print("Password was invalid")


def encryptPasswords(SRCFILESTRING, DESFILESTRING, NONCE, myPassword):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    #from Crypto.Protocol.KDF import scrypt
    myPaddedPassword = pad(myPassword, 32)
    encrypter = AES.new(myPaddedPassword, AES.MODE_GCM)
    with open(NONCE, "wb") as fileobj:
        fileobj.write(encrypter.nonce)
    #Clear the file, but insert nothing here
    with open(DESFILESTRING, 'wb') as myFile:
        myFile.write(b"")
    with open(SRCFILESTRING, "rb") as passwordFile:
        while(True):
            passwordStr = passwordFile.read(1024)
            # Encrypt passwords using the master password
            if(len(passwordStr)==0):
                break
            encLine = encrypter.encrypt(passwordStr)
            with open(DESFILESTRING, 'ab') as myFile:
                myFile.write(encLine)



def decryptPasswords(SRCFILESTRING, DESFILESTRING, NONCE, myPassword):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    myPaddedPassword = pad(myPassword, 32)
    with open(NONCE,'rb') as nonceFile:
        nonce = nonceFile.read(1024)
    with open(DESFILESTRING, 'wb') as myFile:
        myFile.write(b"")
    decrypter = AES.new(myPaddedPassword, AES.MODE_GCM, nonce=nonce)
    with open(SRCFILESTRING, "rb") as passwordFile:
        while(True):
            passwordStr = passwordFile.read(1024)
            if (len(passwordStr) == 0):
                break
            # Decrypt passwords using the master password
            decLine = decrypter.decrypt(passwordStr)
            with open(DESFILESTRING, 'ab') as myFile:
                myFile.write(decLine)


def encryptPasswordWithDictionary(DESFILESTRING, myPassword,NONCE, passwordDict):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    #from Crypto.Protocol.KDF import scrypt
    import json
    from os import remove
    myPaddedPassword = pad(myPassword, 32)
    encrypter = AES.new(myPaddedPassword, AES.MODE_GCM)
    with open(NONCE, "wb") as fileobj:
        fileobj.write(encrypter.nonce)
    #Clear the file, but insert nothing here
    with open(DESFILESTRING, 'wb') as myFile:
        myFile.write(b"")
    SRCFILESTRING = "temp.json"
    with open(SRCFILESTRING, "w") as jsonFile:
        json.dump(passwordDict, jsonFile)
    with open(SRCFILESTRING, "rb") as passwordFile:
        while (True):
            passwordStr = passwordFile.read(1024)
            # Encrypt passwords using the master password
            if (len(passwordStr) == 0):
                break
            encLine = encrypter.encrypt(passwordStr)
            with open(DESFILESTRING, 'ab') as myFile:
                myFile.write(encLine)
    remove(SRCFILESTRING)


def decryptPasswordsToDictionary(SRCFILESTRING, NONCE, myPassword):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    myPaddedPassword = pad(myPassword, 32)
    import json
    from os import remove
    DESFILESTRING = "temp.json"
    with open(NONCE, 'rb') as nonceFile:
        nonce = nonceFile.read(1024)
    with open(DESFILESTRING, 'wb') as myFile:
        myFile.write(b"")
    decrypter = AES.new(myPaddedPassword, AES.MODE_GCM, nonce=nonce)
    with open(SRCFILESTRING, "rb") as passwordFile:
        while (True):
            passwordStr = passwordFile.read(1024)
            if (len(passwordStr) == 0):
                break
            # Decrypt passwords using the master password
            decLine = decrypter.decrypt(passwordStr)
            with open(DESFILESTRING, 'ab') as myFile:
                myFile.write(decLine)
    with open(DESFILESTRING, "r") as jsonFile:
        passwordDict = json.load(jsonFile)
    remove(DESFILESTRING)
    return passwordDict


if(__name__ == '__main__'):
    #TODO Change the relative path names to absolute path names
    encryptPasswords("assets/myPasswords.json", "myPasswords.enc", "nonce.binary", "password".encode())
    #encryptPasswordWithDictionary("passwords.enc", "password".encode(), "assets/nonce.binary",{1:2,3:4,5:6})
    #decryptPasswords("myPasswords.enc", "decrypted.json", "nonce.binary", "password".encode())
    print(decryptPasswordsToDictionary("myPasswords.enc","nonce.binary", "password".encode()))
