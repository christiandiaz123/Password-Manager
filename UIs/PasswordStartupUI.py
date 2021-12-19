from tkinter import *

def startupPassword(root, passwordBtn, confirmPasswordBtn, frame):
    password1 = passwordBtn.get()
    password2 = confirmPasswordBtn.get()
    if(password1 !=password2):
        #print("Passwords do not match, please try again")
        passwordFailedLabel = Label(frame, text="Passwords do not match, please try again")
        passwordFailedLabel.grid(row=4, column=0, pady=5)
        passwordBtn.delete(0, END)
        confirmPasswordBtn.delete(0, END)
    else:
        from hashlib import sha256
        from os import remove
        with open("../assets/hash.txt", "w") as file:
            file.write(sha256(password1.encode("utf-8")).hexdigest())
        with open("temp1.json", "w") as file:
            file.write("{\n\n}")
        from encryptionFunctions import encryptPasswords
        encryptPasswords("temp1.json", "../assets/passwords.enc","../assets/nonce.binary", password1.encode("utf-8"))
        remove("temp1.json")
        from mainmenu import mainMenuFrame
        for widget in root.winfo_children():
            widget.destroy()
        mainMenuFrame(root, {}, password1).pack()


root = Tk()
root.iconbitmap("../assets/favicon.ico")
root.title("Christian Diaz's Password Manager Version 1.0.0")
frame = Frame(root, padx=45, pady=20)

introductionLabel = Label(frame, text="Welcome to your Password Manager.")

passwordFrame = Frame(frame)
passwordLabel = Label(passwordFrame, text="Please enter a Master Password for your Password Manager")
passwordInput = Entry(passwordFrame, show="*")

confirmPasswordFrame = Frame(frame)
confirmPasswordLabel = Label(confirmPasswordFrame, text="Please confirm the Master Password for your Password Manager")
confirmPasswordInput = Entry(confirmPasswordFrame, show="*")

confirmButton = Button(frame, text="Confirm", command=lambda: startupPassword(root, passwordInput,confirmPasswordInput, frame))

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