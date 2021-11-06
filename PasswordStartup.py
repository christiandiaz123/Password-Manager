import os
from hashlib import sha256
while(True):
    print("Please input a Master Password:")
    masterPassword = input()
    print("Confirm your Password:")
    confirmPassword = input()
    if(masterPassword==confirmPassword):
        break
    else:
        print("Passwords do not match")
with open("hash.txt", 'w') as file:
    file.write(sha256(masterPassword.encode()).hexdigest())

