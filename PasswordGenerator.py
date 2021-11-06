import random
import doctest
"""
Password requirements:
greater than or equal to 12 characters in length
less than or equal to 40 characters in length
Must Contain 1 Uppercase Character [A-Z]
Must Contain 1 Lowercase Character[a-z]
Must Contain 1 Digit[0-9]
Optional:
Contains 1 Special Character[!@#$%^&*_]
"""
def passwordGenerator():
    upperCharSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCharSet = "abcdefghijklmnopqrstuvwxyz"
    numCharSet = "0123456789"
    specialCharSet = "!@#$%^&*_"
    charSet = upperCharSet + lowerCharSet + numCharSet + specialCharSet
    listcharSet = list(charSet)
    myPassword = ""
    while(len(myPassword)<27+random.randint(1,8)):
        myPassword += random.choice(listcharSet)
    myPassword = list(myPassword)
    myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(upperCharSet)))
    myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(lowerCharSet)))
    myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(numCharSet)))
    myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(specialCharSet)))
    myPassword = "".join(myPassword)
    return myPassword

if(__name__=="__main__"):
    for _ in range(100):
        myPassword = passwordGenerator()
        print(myPassword)
        print(len(myPassword))
