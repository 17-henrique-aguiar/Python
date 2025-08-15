class Jogador:
    def __init__(self,nome,pontos):
        self.nome = nome
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor

    def exibir_pontos(self):
        print(f"Jogador: {self.nome} | Pontos: {self.pontos}")
