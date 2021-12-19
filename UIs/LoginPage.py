from tkinter import *
root = Tk()
root.title("Christian Diaz's Password Manager Version 1.0.0")
root.iconbitmap("../assets/favicon.ico")
def confirmButtonFunc(root, passwordInput, errLabel):
    from hashlib import sha256
    from mainmenu import mainMenuFrame
    password = passwordInput.get()
    with open("../assets/hash.txt", "r") as file:
        hash1 = file.read()
    if(sha256(password.encode("utf-8")).hexdigest()==hash1):
        from encryptionFunctions import decryptPasswordsToDictionary
        passwordsDictionary = decryptPasswordsToDictionary("../assets/passwords.enc", "../assets/nonce.binary", password.encode("utf-8"))
        print(passwordsDictionary)
        for widget in root.winfo_children():
            widget.destroy()
        frame = mainMenuFrame(root, passwordsDictionary,password)
        frame.grid(row=0,column=0)
    else:
        errLabel.config(text="Password was incorrect")
        passwordInput.delete(0,END)


frame = Frame(root, padx=100, pady=100)
myLabel = Label(frame, text="Please enter your Master Password:")
errLabel = Label(frame, text="")
passwordInput = Entry(frame, show="*")
confirmButton = Button(frame, text="Confirm", command=lambda: confirmButtonFunc(root, passwordInput, errLabel))
myLabel.grid(row=0, column=0, pady=5)
passwordInput.grid(row=1, column=0, pady=5)
confirmButton.grid(row=2, column=0, pady=5)
errLabel.grid(row=3, column=0, pady=5)

frame.grid(row=0, column=0)

root.mainloop()
