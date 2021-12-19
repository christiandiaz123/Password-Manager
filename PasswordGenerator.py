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
def passwordGenerator(startRange, endRange,Flags, SpecialCharacters=None):
    assert isinstance(startRange, int) and isinstance(endRange, int), "Starting and Ending ranges must be of type int"
    assert startRange > 0 and endRange > 0, ""
    assert Flags>0, "At least one flag must be active"
    assert startRange <= endRange, "Start Range must be before End Range"
    upperCharSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCharSet = "abcdefghijklmnopqrstuvwxyz"
    numCharSet = "0123456789"
    specialCharSet = "!@#$%^&*_" if SpecialCharacters == None else SpecialCharacters
    charSet = ""
    myPassword = ""
    myPassword = list(myPassword)
    if(Flags&1):
        myPassword.insert(random.randint(0, len(myPassword)), random.choice(list(lowerCharSet)))
        charSet+=lowerCharSet
    if(Flags&2):
        myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(upperCharSet)))
        charSet+=upperCharSet
    if(Flags&4):
        myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(numCharSet)))
        charSet+=numCharSet
    if(Flags&8):
        myPassword.insert(random.randint(0,len(myPassword)), random.choice(list(specialCharSet)))
        charSet+=specialCharSet
    listcharSet = list(charSet)
    range = startRange + random.randint(0, endRange-startRange)
    while (len(myPassword) < range):
        myPassword += random.choice(listcharSet)
    myPassword = "".join(myPassword)
    return myPassword

if(__name__=="__main__"):
    for _ in range(100):
        myPassword = passwordGenerator(12,30, 12)
        print(myPassword)
        print(len(myPassword))
