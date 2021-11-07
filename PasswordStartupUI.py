from tkinter import *

root = Tk()
root.title("Christian Diaz's Password Manager Version 1.0.0")
frame = Frame(root, padx=45, pady=20)

introductionLabel = Label(frame, text="Welcome to your Password Manager.")

passwordFrame = Frame(frame)
passwordLabel = Label(passwordFrame, text="Please enter a Master Password for your Password Manager")
passwordInput = Entry(passwordFrame)

confirmPasswordFrame = Frame(frame)
confirmPasswordLabel = Label(confirmPasswordFrame, text="Please confirm the Master Password for your Password Manager")
confirmPasswordInput = Entry(confirmPasswordFrame)

confirmButton = Button(frame, text="Confirm")

passwordLabel.grid(row=0, column=0,pady=5)
passwordInput.grid(row=1, column=0,pady=5)

confirmPasswordLabel.grid(row=0, column=0, pady=5)
confirmPasswordInput.grid(row=1,column=0)

introductionLabel.grid(row=0, column=0)
passwordFrame.grid(row=1, column=0, pady=10)
confirmPasswordFrame.grid(row=2, column=0, pady=10)
confirmButton.grid(row=3, column=0, pady=10)

frame.grid(row=0,column=0)

root.mainloop()