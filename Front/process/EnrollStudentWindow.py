
from tkinter import ttk
import tkinter as tk

class EnrollStudentWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Matricula de Aluno")
        self.root.geometry("650x300")
        self.root.resizable(True, True)


    def EnrollStudentWindow(self):

        courselabel = tk.Label(self.root, text="Curso")
        courselabel.place(x=30, y=30)

        coursecbx = ttk.Combobox()
        coursecbx.place(x=100, y=30, width=300, height=25)

        teacherlabel = tk.Label(self.root, text="Professor")
        teacherlabel.place(x=30, y=90)

        teachercbx = ttk.Combobox()
        teachercbx.place(x=100, y=90, width=300, height=25)

        studentlabel = tk.Label(self.root, text="Aluno")
        studentlabel.place(x=30, y=150)

        studentcbx = ttk.Combobox()
        studentcbx.place(x=100, y=150, width=300, height=25)

        subjectlabel = tk.Label(self.root, text="Disciplina")
        subjectlabel.place(x=30, y=210)

        subjectcbx = ttk.Combobox()
        subjectcbx.place(x=100, y=210, width=300, height=25)

        saveButton = tk.Button(self.root, text="Salvar")
        saveButton.place(x=160, y=270, width=100, height=25)

        backButton = tk.Button(self.root, text="Voltar")
        backButton.place(x=270, y=270, width=100, height=25)

        self.root.mainloop()
        #self.root.quit()

if __name__ == "__main__":
    enroll = EnrollStudentWindow()
    enroll.EnrollStudentWindow()