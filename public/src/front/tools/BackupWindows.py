import sys
from tkinter import ttk, messagebox
import tkinter as tk
from public.src.front.PrincipalWindow import *


class BackupWindows:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Backup")
        self.root.geometry("350x200")
        self.root.resizable(True, True)

    def backup_windows_confirmation(self):
        msg = messagebox.askyesno("Backup", "Deseja fazer o backup das informações?")
        if not msg:
            self.root.destroy()
            sys.exit()
            PrincipalWindow().principalWindow()

        backuplabel = tk.Label(self.root, text="Processo de Backup ")
        backuplabel.place(x=120, y=50)

        progressbar = ttk.Progressbar()
        progressbar.place(x=75, y=70, width=200, height=25)
        progressbar.config(maximum=100)

        backButton = tk.Button(self.root, text="Cancelar")
        backButton.place(x=120, y=150, width=100, height=25)

        self.root.mainloop()
