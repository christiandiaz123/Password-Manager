from tkinter import *
from tkinter import ttk
import json
import os
Switch = False
def mainMenuFrame(root, myPasswordsDict, password):
    assert os.path.exists("myPasswords.json"), "Passwords are corrupted or encrypted"
    def generatePasswordFunc(root, passwordDictionary, password):
        from PasswordGeneratorUI import passwordGeneratorUI
        for widget in root.winfo_children():
            widget.destroy()
        mainFrame = passwordGeneratorUI(root,myPasswordsDict, password)
        mainFrame.pack()

    def settingsFunc(root, passwordDictionary, password):
        from SettingUI import SettingUI
        for widget in root.winfo_children():
            widget.destroy()
        mainFrame = SettingUI(root, passwordDictionary, password)
        mainFrame.grid(row=0,column=0)


    def showAndHidePasswords(myFrame, myPasswordDict, myList):
        global Switch
        Switch = not Switch #lol, as a mathematician this feels so dirty
        loc = 1
        for key, val in myPasswordDict.items():
            if (loc == 100):
                break
            myList[loc - 1].configure(text=val if Switch else '*' * len(val))
            loc += 1

    def copyPassword(errLabel, myPasswordDict, key):
        from pyperclip import copy
        if(key in myPasswordDict):
            copy(myPasswordDict[key])
            errLabel.config(text="Password Copied")
        else:
            errLabel.config(text="No Such Key")
        errLabel.grid(row=1, column=0, columnspan=3)
    mainFrame = Frame(root)
    navBarFrame = Frame(mainFrame)
    frame = Frame(mainFrame, highlightbackground="blue", highlightthickness=5)
    frame.grid(row=1, column=0, columnspan=3)
    myCanvas = Canvas(frame, width=600, height=500)
    myCanvas.pack(side=LEFT, fill=BOTH, expand=1)
    myScroll = ttk.Scrollbar(frame, orient=VERTICAL, command=myCanvas.yview)
    myScroll.pack(side=RIGHT, fill=Y)
    myCanvas.configure(yscrollcommand=myScroll.set)
    myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion= myCanvas.bbox("all")))

    secondFrame = Frame(myCanvas)
    myCanvas.create_window((125,0), window=secondFrame, anchor="nw")

    Label(secondFrame, text="Key", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5)
    Label(secondFrame, text="Password", font=("Arial", 12)).grid(row=0, column=1, pady=5, padx=5)
    labelList = []
    loc=1
    for key, val in myPasswordsDict.items():
        if(loc==100):
            print("This")
            break
        Label(secondFrame, text=f'{key}', font=("Arial", 16), background='grey').grid(row=loc, column=0, pady=5, padx=5)
        labelList.append(Label(secondFrame, text='*' * len(val), font=("Arial", 16), background='blue'))
        labelList[-1].grid(row=loc, column=1, pady=5, padx=5)
        loc+=1
    generatePassword = Button(navBarFrame, text="New Password", command=lambda: generatePasswordFunc(mainFrame, myPasswordsDict, password))
    generatePassword.grid(row=0, column=0,  padx=(75,50))
    showPassword = Button(navBarFrame, text="Show Passwords", command=lambda: showAndHidePasswords(secondFrame, myPasswordsDict, labelList))
    showPassword.grid(row=0, column=1, padx=50)
    settingBtn = Button(navBarFrame, text="Settings", command=lambda : settingsFunc(root, myPasswordsDict, password))
    settingBtn.grid(row=0, column=2, padx=50)
    navBarFrame.grid(row=0, column=0, pady=25)

    getPasswordFrame = Frame(mainFrame)
    errLabel = Label(getPasswordFrame, text="")
    getPasswordLabel = Label(getPasswordFrame, text="Enter A Password's Key And Copy It To Your Clipboard:")
    getPasswordEntry = Entry(getPasswordFrame, width=15)
    getPasswordBtn = Button(getPasswordFrame, text="Copy", command=lambda: copyPassword(errLabel, myPasswordsDict, getPasswordEntry.get()))

    getPasswordLabel.grid(row=0,column=0, padx=(15,0))
    getPasswordEntry.grid(row=0, column=1)
    getPasswordBtn.grid(row=0, column=2, padx=(0, 15))
    getPasswordFrame.grid(row=2, column=0, pady=20)
    return mainFrame

if(__name__=="__main__"):
    root = Tk()
    from encryptionFunctions import decryptPasswordsToDictionary
    passwordDict = decryptPasswordsToDictionary("../assets/passwords.enc", "../assets/nonce.binary", "oldPassword".encode("utf-8"))
    mainMenuFrame(root, passwordDict, "oldPassword".encode("utf-8")).grid(row=0,column=0)
    root.mainloop()

