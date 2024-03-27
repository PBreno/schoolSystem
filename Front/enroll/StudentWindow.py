from tkinter import ttk
import tkinter as tk

class StudentWindow():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cadastro Aluno")
        self.root.geometry("750x350")
        self.root.resizable(True, True)

    def studentWindow(self):

        state = list()
        state.append("AC")
        state.append("AL")
        state.append("AP")
        state.append("AM")
        state.append("BA")
        state.append("CE")
        state.append("DF")
        state.append("ES")
        state.append("GO")
        state.append("MA")
        state.append("MT")
        state.append("MS")
        state.append("MG")
        state.append("PA")
        state.append("PB")
        state.append("PR")
        state.append("PE")
        state.append("PI")
        state.append("RJ")
        state.append("RN")
        state.append("RS")
        state.append("RO")
        state.append("RR")
        state.append("SC")
        state.append("SP")
        state.append("SE")
        state.append("TO")

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
        cpfEntry.place(x=20, y=110, width=160, height=25)

        emailLabel = tk.Label(self.root, text="Email")
        emailLabel.place(x=190, y=90)

        emailEntry = tk.Entry()
        emailEntry.place(x=190, y=110, width=160, height=25)

        cepLabel= tk.Label(self.root, text="CEP")
        cepLabel.place(x=20, y=140)

        cepEntry = tk.Entry()
        cepEntry.place(x=20, y=160, width=160, height=25)

        logradouroLabel = tk.Label(self.root, text="Logradouro")
        logradouroLabel.place(x=190, y=140)

        logradouroEntry = tk.Entry()
        logradouroEntry.place(x=190, y=160, width=160, height=25)

        districtlabel= tk.Label(self.root, text="Bairro")
        districtlabel.place(x=20, y=190)

        districtEntry = tk.Entry()
        districtEntry.place(x=20, y=210, width=160, height=25)

        citylabel= tk.Label(self.root, text="Cidade")
        citylabel.place(x=190, y=190)

        cityEntry = tk.Entry()
        cityEntry.place(x=190, y=210, width=160, height=25)

        statelabel= tk.Label(self.root, text="Estado")
        statelabel.place(x=360, y=190)

        statecbx = ttk.Combobox(self.root, values=state)
        statecbx.place(x=360, y=210, width=80, height=25)

        telephonelabel = tk.Label(self.root, text="Telefone")
        telephonelabel.place(x=20, y=240)

        telephoneEntry = tk.Entry()
        telephoneEntry.place(x=20, y=260, width=160, height=25)

        cellphonelabel = tk.Label(self.root, text="Celular")
        cellphonelabel.place(x=190, y=240)

        cellphoneEntry = tk.Entry()
        cellphoneEntry.place(x=190, y=260, width=160, height=25)

        rglabel = tk.Label(self.root, text="RG")
        rglabel.place(x=360, y=240)

        rgEntry = tk.Entry()
        rgEntry.place(x=360, y=260, width=160, height=25)

        saveButton = tk.Button(self.root, text="Salvar")
        saveButton.place(x=220, y=320, width=100, height=25)

        backButton = tk.Button(self.root, text="Voltar")
        backButton.place(x=330, y=320, width=100, height=25)

        self.root.mainloop()


if __name__ == "__main__":
    studentWindow = StudentWindow()
    studentWindow.studentWindow()
