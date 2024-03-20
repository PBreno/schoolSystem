import sys
import tkinter as tk
from tkinter import messagebox

from Front.EnrollUserWindow import EnrollUserWindow
from Front.PrincipalWindow import PrincipalWindow


#Login Class
class LoginWindow():

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Principal")
        self.root.geometry("350x250")
        self.root.resizable(True, True)
        self.checkWindows = None

    #Username and password validation
    def validationForm(self, username: str, password: str):

        try:
            if username == "" or password == "":
                messagebox.showwarning("Username or password is empty",
                                       "Please enter your username and password")
            else:
                #messagebox.showinfo("Success", "Login Successful")
                self.root.destroy()
                PrincipalWindow().principalWindow()
        except:
            messagebox.showerror("Error", "Please enter your username and password")


    def enrollNewUser(self):
        self.root.destroy()
        enrollUser_window = EnrollUserWindow()
        tk.Toplevel(enrollUser_window.enrollUser())
        sys.exit()

    #Login window's interface
    def login(self):

        labelFrame = tk.LabelFrame(self.root, text="Login")
        labelFrame.pack(fill="both", expand=True, padx=5, pady=5)

        titleLabel = tk.Label(labelFrame, text="Sistema Escolar")
        titleLabel.place(x=200, y=10, anchor=tk.CENTER)

        #Username Label
        usernameLabel = tk.Label(self.root, text="Username")
        usernameLabel.place(x=10, y=70)

        #Username input Field
        usernameEntry = tk.Entry()
        usernameEntry.place(x=70, y=70)

        #Password Label
        passwordLabel = tk.Label( self.root, text="Password")
        passwordLabel.place(x=10, y=100)

        #Password input Field
        passwordEntry = tk.Entry(validate="focusout", show="*")
        passwordEntry.place(x=70, y=100)

        enrollLabel = tk.Label(self.root, text="or")
        enrollLabel.place(x=155, y=140, anchor=tk.CENTER)

        loginButton = tk.Button(self.root, text="Login")
        loginButton.place(x=70, y=140)
        loginButton.bind("<Button-1>", lambda event: self.validationForm(usernameEntry.get(), passwordEntry.get()))

        enrollButton = tk.Button(self.root, text="Enroll")
        enrollButton.place(x=180, y=140)
        enrollButton.bind('<Button-1>', lambda event: self.enrollNewUser())

        self.root.mainloop()