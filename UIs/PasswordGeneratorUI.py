from tkinter import *
from PasswordGenerator import passwordGenerator
def passwordGeneratorUI(root, passwordDict, password):
    mainFrame = Frame(root)

    with open("../assets/specialCharacters","r") as charFile:
        SPECIALCHARACTERS = charFile.read()
    def confirmGenPassword(root,start, end,Flags, outputDictionary):
        #print(f"Starting Range:{start}\nEnding Range:{end}\nFlag:{Flags}")
        try:
            start = int(start)
            end = int(end)
        except ValueError:
            #print("Starting and Ending Values must be an Integer")
            outputDictionary["Output Error Label"]["text"] = "Starting and Ending Values must be an Integer"
            return None
        if(start<12 or start>32 or end<12 or end>32):
            #print("Starting and Ending Values must be between 12 and 32(Inclusive)")
            outputDictionary["Output Error Label"]["text"] = "Starting and Ending Values must be between 12 and 32(Inclusive)"
            return None
        if(end<start):
            #print("Starting Value must be less than Ending Value")
            outputDictionary["Output Error Label"]["text"] = "Starting Value must be less than Ending Value"
            return None
        if(Flags==0):
            #print("At least one box must be checked")
            outputDictionary["Output Error Label"]["text"] = "At least one checkbox must be checked"
            return None
        #print(passwordGenerator(start,end,Flags))
        outputDictionary["Output Error Label"]["text"] = ""
        newPassword = passwordGenerator(start, end, Flags)
        outputDictionary["password"] = newPassword
        outputDictionary["Output Label"]["text"] = len(newPassword)*'*' if outputDictionary["bool"] else newPassword
        outputDictionary["Output Display Password Button"]["state"] = "active"
        outputDictionary["Output Copy Button"]["state"] = "active"
        outputDictionary["Set Key Button"]["state"] = "active"
        outputDictionary["Password Was Used"] = False
    def showAndHidePassword(outputDictionary):
        outputDictionary["bool"] = not outputDictionary["bool"]
        outputDictionary["Output Label"]["text"] = len(outputDictionary["password"]) * '*' if outputDictionary["bool"] else outputDictionary["password"]
    def copyPassword(outputDictionary):
        import pyperclip
        pyperclip.copy(outputDictionary["password"])
    def setKey(outputDictionary, passwordDict, password, entry):
        key = entry.get()
        if(key==""):
            outputDictionary["Output Error Label"].config(text="Please Insert A Unique Key To Match To The Password")
        elif(outputDictionary["Password Was Used"]):
            outputDictionary["Output Error Label"].config(text="Please Generate A New Password For Each Key")
        elif(key in passwordDict):
            from tkinter import messagebox
            result = messagebox.askquestion("Key Collision Confirmation", "This key is already being used. If you change it without changing the password first you may lose the account permenantly. Do you wish to continue?")
            if(result == "yes"):
                from encryptionFunctions import encryptPasswordWithDictionary
                passwordDict[key] = outputDictionary["password"]
                outputDictionary["Password Was Used"] = True
                outputDictionary["Output Error Label"].config(text="Password Has Been Set")
                encryptPasswordWithDictionary("../assets/passwords.enc", password.encode("utf-8"), "../assets/nonce.binary", passwordDict)
            else:
                return None
        else:
            from encryptionFunctions import encryptPasswordWithDictionary
            passwordDict[key] = outputDictionary["password"]
            outputDictionary["Password Was Used"] = True
            outputDictionary["Output Error Label"].config(text="Password Has Been Set")
            encryptPasswordWithDictionary("../assets/passwords.enc", password.encode("utf-8"),"../assets/nonce.binary", passwordDict)

    def mainMenu(root, passwordDict, password):
        from mainmenu import mainMenuFrame
        for widget in root.winfo_children():
            widget.destroy()
        frame = mainMenuFrame(root, passwordDict, password)
        frame.grid(row=0, column=0)

    def settingsUI(root, passwordDict, password):
        from SettingUI import SettingUI
        for widget in root.winfo_children():
            widget.destroy()
        frame = SettingUI(root, passwordDict, password)
        frame.grid(row=0, column=0)

    #Navigation Bar
    navBarFrame = Frame(mainFrame)
    mainMenuButton = Button(navBarFrame, text="Main Menu", command=lambda: mainMenu(root, passwordDict, password))
    passwordGeneratorButton = Button(navBarFrame, text="Settings", command=lambda: settingsUI(root, passwordDict, password))
    mainMenuButton.grid(row=0, column=0, padx=50)
    passwordGeneratorButton.grid(row=0, column=1, padx=50)
    navBarFrame.grid(row=0, column=0, columnspan=2, pady=15)

    outputFrame = Frame(mainFrame)
    outputDictionary = {}
    outputDictionary["bool"] = True
    outputLabel = Label(outputFrame, text="(Output Password Here)", width=32)
    outputDictionary["Output Label"] = outputLabel
    outputDisplayPasswordButton = Button(outputFrame, text="Show", command=lambda: showAndHidePassword(outputDictionary))
    outputDictionary["Output Display Password Button"] = outputDisplayPasswordButton
    outputDisplayPasswordButton["state"] = "disable"
    outputCopyButton = Button(outputFrame, text="Copy", command=lambda: copyPassword(outputDictionary))
    outputDictionary["Output Copy Button"] = outputCopyButton
    outputCopyButton["state"] = "disable"
    outputLabel.grid(row=0, column=0)
    outputDisplayPasswordButton.grid(row=0, column=1)
    outputCopyButton.grid(row=0, column=2)
    outputFrame.grid(row=2, column=0)

    rangeFrame = Frame(mainFrame)
    keyLabel = Label(rangeFrame, text="Key(Optional):")
    keyEntry = Entry(rangeFrame, width=15)
    setKeyButton = Button(rangeFrame, text="Set Key", command=lambda: setKey(outputDictionary, passwordDict, password, keyEntry))
    setKeyButton["state"] = "disable"
    outputDictionary["Set Key Button"] = setKeyButton
    startingRange = Entry(rangeFrame, width=10)
    startingRange.insert(END, '12')
    startingRangeLabel = Label(rangeFrame, text="Starting Range:")
    endingRange = Entry(rangeFrame, width=10)
    endingRange.insert(END, '32')
    endingRangeLabel = Label(rangeFrame, text="Ending Range:")
    keyLabel.grid(row=0, column=0, padx=(20,0))
    keyEntry.grid(row=0, column=1, padx=(0,10))
    setKeyButton.grid(row=0, column=3, padx=(0,10))
    startingRangeLabel.grid(row=0, column=4, padx=(20,0))
    startingRange.grid(row=0, column=5)
    endingRangeLabel.grid(row=0, column=6, padx=(20,0))
    endingRange.grid(row=0, column=7, padx=(0,20))
    rangeFrame.grid(row=1,column=0, pady=10, columnspan=2)

    checkbuttonFrame = Frame(mainFrame)
    lowercaseLettersVar = IntVar(value=1)
    lowercaseLetters = Checkbutton(checkbuttonFrame, text="Lowercase Letters", variable=lowercaseLettersVar, command=lambda: lowercaseLettersVar.get())

    uppercaseLettersVar = IntVar(value=1)
    uppercaseLetters = Checkbutton(checkbuttonFrame, text="Uppercase Letters", variable=uppercaseLettersVar, command=lambda: uppercaseLettersVar.get())

    numbersVar = IntVar(value=1)
    numbers = Checkbutton(checkbuttonFrame, text="Numbers", variable=numbersVar, command=lambda: numbersVar.get())

    specialCharactersVar = IntVar(value=0)
    specialCharacters = Checkbutton(checkbuttonFrame, text=f"Special Characters({SPECIALCHARACTERS})", variable=specialCharactersVar, command=lambda: specialCharactersVar.get())

    lowercaseLetters.grid(row=0, column=0, sticky=W)
    uppercaseLetters.grid(row=1, column=0, sticky=W)
    numbers.grid(row=2, column=0, sticky=W)
    specialCharacters.grid(row=3, column=0, sticky=W)
    checkbuttonFrame.grid(row=2, column=1)
    btnFrame = Frame(mainFrame)
    button = Button(btnFrame, text="Confirm", command=lambda: confirmGenPassword(mainFrame, startingRange.get(), endingRange.get(), (lowercaseLettersVar.get()+2*uppercaseLettersVar.get()+4*numbersVar.get()+8*specialCharactersVar.get()), outputDictionary))
    button.grid(row=0, column=0, columnspan=2, pady=10)
    outputErrLabel = Label(btnFrame, text="")
    outputDictionary["Output Error Label"] = outputErrLabel
    outputErrLabel.grid(row=1, column=0)
    btnFrame.grid(row=4, column=0, columnspan=2)
    return mainFrame
if(__name__ == "__main__"):
    root=Tk()
    from encryptionFunctions import decryptPasswordsToDictionary
    passwordDict = decryptPasswordsToDictionary("../assets/passwords.enc", "../assets/nonce.binary", "newpassword".encode("utf-8"))
    passwordGeneratorUI(root, passwordDict, "newpassword").pack()
    root.mainloop()