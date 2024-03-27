import tkinter as tk
from tkinter import messagebox

from Front.PrincipalWindow import PrincipalWindow


class CourseWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro de curso")
        self.root.geometry("450x350")
        self.root.resizable(True, True)


    def backbutton(self, course:str, enrollcost: float, creditvalue:int):

        if course == "" or enrollcost == "" or creditvalue == "":
            msg = messagebox.askyesno("Campos vazios", "Tem a certeza que deseja voltar ?")

            if msg:
                self.root.destroy()
                PrincipalWindow().principalWindow()
        else:
            self.root.destroy()
            PrincipalWindow().principalWindow()

    def courseWindow(self):

        #Course Label
        courseLabel = tk.Label(self.root, text="Curso")
        courseLabel.place(x=20, y=60)

        courseEntry = tk.Entry()
        courseEntry.place(x=60, y= 60, width= 230, height= 25)

        #enroll cost
        enrollCostLabel = tk.Label(self.root, text="Valor da matrícula")
        enrollCostLabel.place(x=20, y=95)

        enrollCostEntry = tk.Entry()
        enrollCostEntry.place(x=130, y=95, width= 230, height= 25)
        enrollCostEntry.insert(1, "0.0")

        # Credit cost
        creditCostLabel = tk.Label(self.root, text="Valor do crédito")
        creditCostLabel.place(x=20, y=125)

        creditCostEntry = tk.Entry()
        creditCostEntry.place(x=130, y=125, width=230, height=25)
        creditCostEntry.insert(1, "0")

        saveButton = tk.Button(self.root, text="Salvar")
        saveButton.place(x=130, y=250, width=100, height=25)

        backButton = tk.Button(self.root, text="Voltar")
        backButton.place(x=240, y=250, width=100, height=25)
        backButton.bind("<Button-1>", lambda event: self.backbutton(courseEntry.get(), float(enrollCostEntry.get()), int(creditCostEntry.get())))


        self.root.mainloop()



# if __name__ == "__main__":
#     courseWindow = CourseWindow()
#     courseWindow.courseWindow()