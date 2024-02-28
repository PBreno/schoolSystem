import tkinter as tk
from tkinter import ttk, messagebox


class EnrollUserWindow():

    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("Cadastro de Usuarios")
        self.root.geometry("350x300")
        self.root.resizable(True,True)

    def saveUser(self, fullName: str, email:str, password:str):

        try:
              if fullName == "" or email == "" or password == "":
                  messagebox.showwarning("Campos vazios","Todos os campos precisam ser preenchidos!")


        except Exception as e:
            messagebox.showerror("Erro", f'{e}')
    def enrollUser(self):

        labelFrame = ttk.LabelFrame(self.root, text="Cadastro de Usuarios")
        labelFrame.pack(fill="both", expand=True, padx=5, pady=5)

        fullNameLabel = ttk.Label(self.root, text="Nome completo")
        fullNameLabel.place(x=10, y=50)

        fullNameEntry = ttk.Entry()
        fullNameEntry.place(x=115, y=50, width=170, height=25)

        emailLabel = ttk.Label(self.root, text="Email")
        emailLabel.place(x=10, y=80)

        emailEntry = ttk.Entry()
        emailEntry.place(x=115, y=80, width=170, height=25)

        passwordLabel = ttk.Label(self.root, text="Senha")
        passwordLabel.place(x=10, y=110)

        passwordEntry = ttk.Entry()
        passwordEntry.place(x=115, y=110, width=170, height=25)

        saveButton = ttk.Button(self.root, text="Salvar")
        saveButton.place(x=100, y=170)
        saveButton.bind("<Button-1>", lambda event:  self.saveUser(fullNameEntry.get(), emailEntry.get(), passwordEntry.get()))

        cancelButton = ttk.Button(self.root, text="Cancelar")
        cancelButton.place(x=190, y=170)
        cancelButton.bind("<Button-1>", lambda event:self)

        #userNameLabel = ttk.Label(labelFrame, text="Usuário")
        #userNameLabel.place(x=10, y=50)

        self.root.mainloop()


#if __name__ == "__main__":
 #   app = EnrollUserWindow()
  #  app.enrollUser()