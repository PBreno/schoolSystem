import tkinter as tk
from tkinter import ttk, messagebox

#Login Class
class LoginWindow():

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Principal")
        self.root.geometry("350x250")
        self.root.resizable(True, True)

    #Username and password validation
    def validationForm(self, username, password):

        try:
            if username == "" or password == "" :
                messagebox.showwarning("Username or password is empty",
                                       "Please enter your username and password")
            else:
                messagebox.showinfo("Success", "Login Successful")
        except:
            messagebox.showerror("Error", "Please enter your username and password")

    #Login window's interface
    def login(self):

        labelFrame = ttk.LabelFrame(self.root, text="Login")
        labelFrame.pack(fill="both", expand=True, padx=5, pady=5)

        #Username Label
        usernameLabel = ttk.Label(self.root, text="Username")
        usernameLabel.place(x=10, y=50)

        #Username input Field
        usernameEntry = ttk.Entry()
        usernameEntry.place(x=70, y=50)

        #Password Label
        passwordLabel = ttk.Label( self.root, text="Password")
        passwordLabel.place(x=10, y=80)

        #Password input Field
        passwordEntry = ttk.Entry()
        passwordEntry.place(x=70, y=80)


        loginButton = ttk.Button(self.root, text="Login")
        loginButton.place(x=70, y=120)
        loginButton.bind("<Button-1>", lambda event: self.validationForm(usernameEntry.get(), passwordEntry.get()))

        self.root.mainloop()