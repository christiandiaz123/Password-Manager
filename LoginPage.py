from tkinter import *

root = Tk()
root.title("Christian Diaz's Password Manager Version 1.0.0")

def confirmButtonFunc(passwordInput, frame):
    from hashlib import sha256
    password = passwordInput.get()
    with open("hash.txt", "r") as file:
        hash1 = file.read()
    if(sha256(password.encode("utf-8")).hexdigest()==hash1):
        print("password is correct")
    else:
        print("password is incorrect")

frame = Frame(root, padx=100, pady=100)
myLabel = Label(frame, text="Please enter your Master Password")
passwordInput = Entry(frame, show="*")
confirmButton = Button(frame, text="Confirm", command=lambda: confirmButtonFunc(passwordInput, frame))
myLabel.grid(row=0, column=0, pady=5)
passwordInput.grid(row=1, column=0, pady=5)
confirmButton.grid(row=2, column=0, pady=5)

frame.grid(row=0, column=0)

root.mainloop()
