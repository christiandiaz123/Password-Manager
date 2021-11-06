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
def encryptPasswords(SRCFILESTRING, DESFILESTRING, myPassword):
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    #from Crypto.Protocol.KDF import scrypt
    myPaddedPassword = pad(myPassword, 32)
    encrypter = AES.new(myPaddedPassword, AES.MODE_GCM)
    with open("nonce.binary", "wb") as fileobj:
        fileobj.write(encrypter.nonce)
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


#encrypter = AES.new(myPaddedPassword, AES.MODE_GCM, nonce=nonce)
#decLine = encrypter.decrypt(encLine)
#print(decLine.decode("utf-8"))