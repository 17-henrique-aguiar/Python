import tkinter as tk
from models import Funcionario, Empresa

class AppCadastro:
    def __init__(self, master, empresa: Empresa):
        self.master = master
        self.empresa = empresa

        master.title("Cadastro de Funcionários")

        # Campos do fomulário
        tk.Label(master, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(master)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Cargo:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_cargo = tk.Entry(master)
        self.entry_cargo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Idade:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_idade = tk.Entry(master)
        self.entry_idade.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(master, text="Salário:").grid(row=3, column=0, padx=5, pady=5)
        self.entry_salario = tk.Entry(master)
        self.entry_salario.grid(row=3, column=1, padx=5, pady=5)

        # Botão salvar
        self.btn_salvar = tk.Button(master, text="Salvar Funcionário", command=self.salvar_funcionario)
        self.btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

        # Mensagem de status
        self.label_status = tk.Label(master, text="", fg="green")
        self.label_status.grid(row=5, column=0, columnspan=2)

    def salvar_funcionario(self):
        """Cria objeto Funcionario e salva na Empresa"""
        nome = self.entry_nome.get()
        cargo = self.entry_cargo.get()
        idade = self.entry_idade.get()
        salario = self.entry_salario.get()

        if nome and cargo and idade and salario:
            funcionario = Funcionario(nome, cargo, idade, salario)
            self.empresa.adicionar_funcionario(funcionario)

            self.label_status.config(text="Funcionário cadastrado com sucesso!", fg="green")

            # limpa os campos
            self.entry_nome.delete(0, tk.END)
            self.entry_cargo.delete(0, tk.END)
            self.entry_idade.delete(0, tk.END)
            self.entry_salario.delete(0, tk.END)
        else:
            self.label_status.config(text="Preencha todos os campos!", fg="red")


if __name__ == "__main__":
    empresa = Empresa()
    root = tk.Tk()
    app = AppCadastro(root, empresa)
    root.mainloop()