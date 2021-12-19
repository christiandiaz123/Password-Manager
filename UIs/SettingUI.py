from tkinter import *
def SettingUI(root, passwordDict, password):
    mainFrame = Frame(root)
    with open("..\\assets\\specialCharacters", 'r') as file:
        SPECIALCHARACTERS = file.read()

    errLabel = Label(mainFrame, text="")
    def changePassword(root, entries, errLabel, passwordDict):
        #Check if Old Passwords Match
        from hashlib import sha256
        oldPassword = entries["Old Password"].get()
        with open("../assets/hash.txt", "r") as file:
            hash1 = file.read()
        if (sha256(oldPassword.encode("utf-8")).hexdigest() == hash1):
            if(entries["New Password"].get()==entries["Confirm Password"].get()):
                #Encrypt Json with New Password
                from encryptionFunctions import encryptPasswordWithDictionary
                encryptPasswordWithDictionary("../assets/passwords.enc", entries["New Password"].get().encode("utf-8"),"../assets/nonce.binary", passwordDict)
                with open("../assets/hash.txt", "w") as file:
                    file.write(sha256(entries["New Password"].get().encode("utf-8")).hexdigest())
                errLabel.config(text="New Password Has Been Set")
            else:
                errLabel.config(text="New Passwords Do Not Match")

        else:
            errLabel.config(text="Password is incorrect")
        errLabel.grid(row=2, column=0, columnspan=2)

    def changeSpecial(root, characters, errLabel, label):
        characters = "".join(set(characters))
        with open("..\\assets\\specialCharacters", 'w') as file:
            file.write(characters)
        errLabel.config(text="New Special Characters Have Been Set")
        label.config(text=f"Enter Special Characters({characters}):")
        errLabel.grid(row=2, column=0, columnspan=2)

    def mainMenu(root, passwordDict, password):
        from mainmenu import mainMenuFrame
        for widget in root.winfo_children():
            widget.destroy()
        frame = mainMenuFrame(root, passwordDict, password)
        frame.grid(row=0, column=0)
    def generatePasswordUI(root, passwordDict, password):
        from PasswordGeneratorUI import passwordGeneratorUI
        for widget in root.winfo_children():
            widget.destroy()
        frame = passwordGeneratorUI(root, passwordDict, password)
        frame.grid(row=0, column=0)

    #Navigation Bar
    navBarFrame = Frame(mainFrame)
    mainMenuButton = Button(navBarFrame, text="Main Menu", command=lambda: mainMenu(root, passwordDict, password))
    passwordGeneratorButton = Button(navBarFrame, text="New Password", command=lambda: generatePasswordUI(root, passwordDict, password))
    mainMenuButton.grid(row=0, column=0, padx=50)
    passwordGeneratorButton.grid(row=0, column=1, padx=50)
    navBarFrame.grid(row=0, column=0, columnspan=2, pady=15)

    #change Master Password Frame
    changePasswordEntry = {}
    changePasswordFrame = Frame(mainFrame)
    changePasswordLabel = Label(changePasswordFrame, text="Change Master Password:")
    oldPasswordLabel = Label(changePasswordFrame, text="Enter Old Password:")
    oldPasswordEntry = Entry(changePasswordFrame, width=16, show='*')
    changePasswordEntry["Old Password"] = oldPasswordEntry
    newPasswordLabel = Label(changePasswordFrame, text="Enter New Password:")
    newPasswordEntry = Entry(changePasswordFrame, width=16, show='*')
    changePasswordEntry["New Password"] = newPasswordEntry
    confirmPasswordLabel = Label(changePasswordFrame, text="Confirm New Password:")
    confirmPasswordEntry = Entry(changePasswordFrame, width=16, show='*')
    changePasswordEntry["Confirm Password"] = confirmPasswordEntry
    confirmButton = Button(changePasswordFrame, text="Confirm", command= lambda: changePassword(mainFrame, changePasswordEntry, errLabel, passwordDict))

    changePasswordLabel.grid(row=0, column=0, columnspan=2)
    oldPasswordLabel.grid(row=1, column=0, pady=15)
    oldPasswordEntry.grid(row=1, column=1, pady=15)
    newPasswordLabel.grid(row=2, column=0, pady=(0,15))
    newPasswordEntry.grid(row=2, column=1, pady=(0,15))
    confirmPasswordLabel.grid(row=3, column=0, pady=(0,15))
    confirmPasswordEntry.grid(row=3, column=1, pady=(0,15))
    confirmButton.grid(row=4, column=0, columnspan=2, pady=(0,15))
    changePasswordFrame.grid(row=1, column=0, padx=25)

    #change Special Characters
    changeSpecialFrame = Frame(mainFrame)
    changeSpecialLabelAndEntryFrame = Frame(changeSpecialFrame)
    changeSpecialLabel = Label(changeSpecialLabelAndEntryFrame, text=f"Enter Special Characters({SPECIALCHARACTERS}):")
    changeSpecialEntry = Entry(changeSpecialLabelAndEntryFrame, width=16)
    changeSpecialButton = Button(changeSpecialFrame, text="Confirm", command=lambda:changeSpecial(mainFrame, changeSpecialEntry.get(), errLabel, changeSpecialLabel))

    changeSpecialLabel.grid(row=0, column=0)
    changeSpecialEntry.grid(row=0, column=1)
    changeSpecialLabelAndEntryFrame.grid(row=1, column=0, pady=15)
    changeSpecialButton.grid(row=2, column=0)
    changeSpecialFrame.grid(row=1, column=1, padx=(0,25))
    return mainFrame
if(__name__=="__main__"):
    root = Tk()
    from encryptionFunctions import decryptPasswordsToDictionary

    passwordDict = decryptPasswordsToDictionary("../assets/passwords.enc", "../assets/nonce.binary", "oldPassword".encode("utf-8"))
    SettingUI(root, passwordDict, "oldPassword").grid(row=0,column=0)
    root.mainloop()
