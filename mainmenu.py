from tkinter import *
from tkinter import ttk
import json
import os

assert os.path.exists("myPasswords.json"), "Passwords are corrupted or encrypted"
Switch = False
def showAndHidePasswords(myFrame, myPasswordDict, myList):
    global Switch
    Switch = not Switch #lol, as a mathematician this feels so dirty
    loc = 1
    for key, val in myPasswordDict.items():
        if (loc == 100):
            break
        myList[loc - 1].configure(text=val if Switch else '*' * len(val))
        loc += 1



with open("myPasswords.json", "r") as file:
    myPasswordsDict = json.load(file)

root = Tk()
frame = Frame(root)
frame.grid(row=1, column=0, columnspan=3)
myCanvas = Canvas(frame)
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
    Label(secondFrame, text=f'{key}', font=("Arial", 16)).grid(row=loc, column=0, pady=5, padx=5)
    labelList.append(Label(secondFrame, text='*' * len(val), font=("Arial", 16)))
    labelList[-1].grid(row=loc, column=1, pady=5, padx=5)
    loc+=1
generatePassword = Button(root, text="New Password")
generatePassword.grid(row=0, column=0)
showPassword = Button(root, text="Show Passwords", command=lambda: showAndHidePasswords(secondFrame, myPasswordsDict, labelList))
showPassword.grid(row=0, column=1)
changePassword =Button(root, text="Change a Password")
changePassword.grid(row=0, column=2)



root.mainloop()

