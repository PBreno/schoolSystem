import tkinter as tk


class PrincipalWindow():
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.root.title("System Escolar")
        self.root.geometry("1150x650")
        self.root.resizable(True, True)
        ##self.root.attributes("-fullscreen", True)

    def showMenu(self):
        menu = tk.Menu(self.root)

        sistema = tk.Menu(menu, tearoff=0)
        cadastro = tk.Menu(menu, tearoff=0)
        processos = tk.Menu(menu, tearoff=0)
        ferramentas = tk.Menu(menu, tearoff=0)

        sistema.add_command(label="Usuários")
        sistema.add_command(label="Sair")

        cadastro.add_command(label="Aluno")
        cadastro.add_command(label="Disciplina")
        cadastro.add_command(label="Professor")
        cadastro.add_command(label="Curso")

        processos.add_command(label="Matricular")

        ferramentas.add_command(label="Backup")
        ferramentas.add_command(label="Replicador")

        menu.add_cascade(label="System", menu=sistema)
        menu.add_cascade(label="Cadastro", menu=cadastro)
        menu.add_cascade(label="Processos", menu=processos)
        menu.add_cascade(label="Ferramentas", menu=ferramentas)

        self.root.config(menu=menu)

    def principalWindow(self):
        self.showMenu()
        self.root.mainloop()
        self.root.quit()


# if __name__ == "__main__":
#     app = PrincipalWindow()
#     app.principalWindow()
