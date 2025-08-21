class Produto:
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    
    def nome_get(self):
        return self._nome
    
    def nome_set(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._nome = novo_nome
        else:
            print("Nome inválido!")

    
    def preco_get(self):
        return self._preco
    
    def preco_set(self,novo_preco):
        if isinstance(novo_preco, (float)) and novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Preço inválidos!")
