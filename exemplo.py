# Getters são métodos usados para ler (ou obter) o valor de um atributo de uma classe.
# Setters são métodos usados para modificar (ou definir) o valor de um atributo.
# Servem para controlar o acesso aos atributos, especialmente quando você quer proteger dados (encapsulamento) ou validar valores antes de atribuí-los.

class Pessoa:
    def __init__(self,nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip() != "":
            self._nome = novo_nome
        else:
            print("Nome inválido!")

p = Pessoa("Ana")
print(p.nome)
p.nome = "Maria"
print(p.nome)