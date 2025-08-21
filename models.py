import csv
import os

class Funcionario:
    def __init__(self, nome, cargo, idade, salario):
        self.nome = nome
        self.cargo = cargo
        self.idade = idade
        self.salario = salario

    def to_list(self):
        """Retorna os dados do funcionário em lista para salvar no CSV"""
        return[self.nome, self.cargo, self.idade, self.salario]
    
class Empresa:
    def __init__(self, nome_arquivo="funcionarios.csv"):
        self.nome_arquivo = nome_arquivo

        # cria o arquivo CSV com cabeçalhos se não existir
        if not os.path.exists(self.nome_arquivo):
            with open(self.nome_arquivo, mode="w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["Nome", "Cargo", "Idade", "Salário"])
    
    def adicionar_funcionario(self, funcionario: Funcionario):
        """Adiciona funcionários no arquivo CVS"""
        with open(self.nome_arquivo, mode="a", newline="", encoding="utf-8") as f:
            escritor = csv.writer(f)
            escritor.writerow(funcionario.to_list())
    