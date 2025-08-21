# 1
class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_dados(self):
        print(f"Titulo: {self.titulo} | Autor: {self.autor}")

class Usuario:
    def __init__(self,nome,codigo):
        self.nome = nome
        self.codigo = codigo
    
    def exibir_usu(self):
        print(f"Usuário: {self.nome} | Código: {self.codigo}")

