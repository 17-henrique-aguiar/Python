import tkinter as tk
from tkinter import ttk
from  PIL import Image, ImageTk

class Aluno:
    def __init__(self, nome, idade, serie):
        self.nome = nome
        self.idade = idade
        self.serie = serie

    def to_tuple(self):
        return (self.nome, self.idade, self.serie)
    
class SistemaEscola:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Escolar - EFG")
        self.root.geometry("800x400")
        self.root.configure(bg="yellow")

        self.alunos = []

        # Exibir logo no topo
        img = Image.open("c5cc96e2-754e-4116-b769-9d1dbff2c329.png")
        img = img.resize((80, 80))  # Redimensiona
        self.logo = ImageTk.PhotoImage(img)     #   Converte para o formato Tkinter

        lbl_logo = tk.Label(self.root, image=self.logo, bg="yellow")
        lbl_logo.place(x=10, y=10)      # Posição no canto superior esquerdo

        # Frame principal

        frame_principal = tk.Frame(self.root, bg="yellow")
        frame_principal.pack(fill="both", expand=True, pady=20, padx=120)     # Deixa espaço para o logo

        # Formulário (esquerda)
        frame_form = tk.Frame(frame_principal, bg="yellow", pady=10, padx=10)
        frame_form.pack(side="left", fill="y")

        tk.Label(frame_form, text="Nome:", bg="yellow", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_name = tk.Entry(frame_form)
        self.entry_name.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Idade:", bg="yellow", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_idade = tk.Entry(frame_form)
        self.entry_idade.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Série:", bg="yellow", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_serie = tk.Entry(frame_form)
        self.entry_serie.grid(row=2, column=1, pady=5)

        btn_add = tk.Button(frame_form, text="Registrar Aluno", bg="orange", fg="black", font=("Arial", 10, "bold"), command=self.adicionar_aluno)
        btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Tabela (direita)
        frame_tabela = tk.Frame(frame_principal, bg="yellow", padx=10, pady=10)
        frame_tabela.pack(side="right", fill="both", expand=True)

        colunas = ("nome", "idade", "serie")
        self.tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings")

        self.tree.heading("nome", text="Nome")
        self.tree.heading("idade", text="Idade")
        self.tree.heading("serie", text="Série")

        self.tree.column("nome", width=150)
        self.tree.column("idade", width=80)
        self.tree.column("serie", width=100)

        scrollbar = ttk.Scrollbar(frame_tabela, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        self.tree.pack(fill="both", expand=True)

    def adicionar_aluno(self):
        nome = self.entry_name.get()
        idade = self.entry_idade.get()
        serie = self.entry_serie.get()

        if nome and idade and serie:
            aluno = Aluno(nome, idade, serie)
            self.alunos.append(aluno)
            self.tree.insert("", "end", values=aluno.to_tuple())

            self.entry_name.delete(0,tk.END)
            self.entry_idade.delete(0,tk.END)
            self.entry_serie.delete(0,tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaEscola(root)
    root.mainloop()