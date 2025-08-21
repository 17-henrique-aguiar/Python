# Exemplo
class Pessoa:
    ano_atual = 2025

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self)
        print(self.ano_atual - self.idade)

p1 = Pessoa('Eduardo', 33)
p1.get_ano_nascimento()


# # 01
# class Saldo:
#     desconto = 15

#     def __init__(self,nome,saldo_atual):
#         self.nome = nome
#         self.saldo_atual = saldo_atual
    
#     def calculo(self):
#         print(self.saldo_atual - self.desconto)
    
# saldo_final = Saldo('Sandro', 50)
# saldo_final.calculo()

# 02
# class Compra:
#     valor_conta = 200

#     def __init__(self,nome,valorT):
#         self.nome = nome
#         self.valorT = valorT

#     def valor_final(self):
#         print(self.valor_conta - self.valorT)

# venda1 = Compra('Luiz', 80)
# venda1.valor_final()
