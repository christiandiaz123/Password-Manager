from tkinter import *

def startupPassword(passwordBtn, confirmPasswordBtn, frame):
    password1 = passwordBtn.get()
    password2 = confirmPasswordBtn.get()
    if(password1 !=password2):
        #print("Passwords do not match, please try again")
        passwordFailedLabel = Label(frame, text="Passwords do not match, please try again")
        passwordFailedLabel.grid(row=4, column=0, pady=5)
    else:
        from hashlib import sha256
        with open("myPasswords.json", "w") as file:
            file.write("{\n\n}")
        with open("hash.txt", "w") as file:
            file.write(sha256(password1.encode("utf-8")).hexdigest())

root = Tk()
root.title("Christian Diaz's Password Manager Version 1.0.0")
frame = Frame(root, padx=45, pady=20)

introductionLabel = Label(frame, text="Welcome to your Password Manager.")

passwordFrame = Frame(frame)
passwordLabel = Label(passwordFrame, text="Please enter a Master Password for your Password Manager")
passwordInput = Entry(passwordFrame, show="*")

confirmPasswordFrame = Frame(frame)
confirmPasswordLabel = Label(confirmPasswordFrame, text="Please confirm the Master Password for your Password Manager")
confirmPasswordInput = Entry(confirmPasswordFrame, show="*")

confirmButton = Button(frame, text="Confirm", command=lambda: startupPassword(passwordInput,confirmPasswordInput, frame))

passwordLabel.grid(row=0, column=0,pady=5)
passwordInput.grid(row=1, column=0,pady=5)

confirmPasswordLabel.grid(row=0, column=0, pady=5)
confirmPasswordInput.grid(row=1, column=0)

introductionLabel.grid(row=0, column=0)
passwordFrame.grid(row=1, column=0, pady=10)
confirmPasswordFrame.grid(row=2, column=0, pady=10)
confirmButton.grid(row=3, column=0, pady=10)

frame.grid(row=0,column=0)

root.mainloop()