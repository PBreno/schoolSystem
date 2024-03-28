import tkinter as tk
from tkinter import ttk


class SubjectWindow:
    def __init__(self):
        self.__init__()
        self.root = tk.Tk()
        self.root.title("Cadastro de Disciplina")
        self.root.geometry("450x350")
        self.root.resizable(True, True)

    def subject_window(self):

        subjectLabel = tk.Label(self.root, text="Disicplina", font=("Times New Roman", 15))
        subjectLabel.place(x=20, y=60)

        subjectEntry = tk.Entry()
        subjectEntry.place(x=150, y=60, width=230, height=25)

        teacherLabel = tk.Label(self.root, text="Professor", font=("Times New Roman", 15))
        teacherLabel.place(x=20, y=95)

        teachercbx = ttk.Combobox()
        teachercbx.place(x=150, y=95, width=230, height=25)

        workloadLabel = tk.Label(self.root, text="Carga Horária", font=("Times New Roman", 15))
        workloadLabel.place(x=20, y=125)

        workloadEntry = tk.Entry()
        workloadEntry.place(x=150, y=125, width=230, height=25)

        creditLabel = tk.Label(self.root, text="Créditos", font=("Times New Roman", 15))
        creditLabel.place(x=20, y=155)

        creditEntry = tk.Entry()
        creditEntry.place(x=150, y=155, width=230, height=25)

        saveButton = tk.Button(self.root, text="Salvar")
        saveButton.place(x=130, y=250, width=100, height=25)

        backButton = tk.Button(self.root, text="Voltar")
        backButton.place(x=240, y=250, width=100, height=25)
        backButton.bind("<Button-1>", lambda event: self)

        self.root.mainloop()
