class ContaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular = titular
        self.__saldo = saldo

    # Método para depositar
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    # Método para saque
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
    # Getter para saldo
    def get_saldo(self):
        return self.__saldo