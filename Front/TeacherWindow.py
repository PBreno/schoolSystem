from tkinter import ttk
import tkinter as tk

class TeacherWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro Professor")
        self.root.geometry("450x350")
        self.root.resizable(True, True)


    def teacherWindow(self):

        enrollmentLabel = tk.Label(self.root, text="Matrícula", font=("Times New Roman", 15))
        enrollmentLabel.grid(row=0, column=0)

        enrollmentEntry = tk.Entry()
        enrollmentEntry.grid(row=0, column=1)

        nameLabel = tk.Label(self.root, text="Nome", font=("Times New Roman",15))
        nameLabel.grid(row=1, column=0)

        nameEntry = tk.Entry()
        nameEntry.grid(row=1, column=1)

        birthdayLabel = tk.Label(self.root, text="Nascimento", font=("Times New Roman", 15))
        birthdayLabel.grid(row=2, column=0)

        genderLabel = tk.Label(self.root, text="Sexo", font=("Times New Roman", 15))
        genderLabel.grid(row=3, column=0)


        self.root.mainloop()

if __name__ == "__main__":
    teacherWindow = TeacherWindow()
    teacherWindow.teacherWindow()
