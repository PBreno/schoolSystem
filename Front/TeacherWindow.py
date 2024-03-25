from tkinter import ttk
import tkinter as tk

class TeacherWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro Professor")
        self.root.geometry("700x400")
        self.root.resizable(True, True)


    def teacherWindow(self):

        enrollmentLabel = tk.Label(self.root, text="Matrícula")
        enrollmentLabel.place(x=20, y=40)

        enrollmentEntry = tk.Entry()
        enrollmentEntry.place(x=20, y=60, width=60, height=25)

        nameLabel = tk.Label(self.root, text="Nome")
        nameLabel.place(x=100, y=40)

        nameEntry = tk.Entry()
        nameEntry.place(x=100, y=60, width=200, height=25)

        birthdayLabel = tk.Label(self.root, text="Nascimento")
        birthdayLabel.place(x=320, y=40)

        birthdayEntry = tk.Entry()
        birthdayEntry.place(x=320, y=60, width=160, height=25)

        genderLabel = tk.Label(self.root, text="Sexo")
        genderLabel.place(x=530, y=40)

        radiovar =tk.BooleanVar(value=False)

        genderM_radio = tk.Radiobutton(self.root, text="M", value='M', variable=radiovar)
        genderM_radio.place(x=530, y=60)

        genderF_radio = tk.Radiobutton(self.root, text="F", value='F', variable=radiovar)
        genderF_radio.place(x=580, y=60)

        cpfLabel = tk.Label(self.root, text="CPF")
        cpfLabel.place(x=20, y=90)

        cpfEntry = tk.Entry()
        cpfEntry.place(x=20, y=110, width=130, height=25)

        emailLabel = tk.Label(self.root, text="Email")
        emailLabel.place(x=170, y=90)

        emailEntry = tk.Entry()
        emailEntry.place(x=170, y=110, width=160, height=25)

        self.root.mainloop()

if __name__ == "__main__":
    teacherWindow = TeacherWindow()
    teacherWindow.teacherWindow()
