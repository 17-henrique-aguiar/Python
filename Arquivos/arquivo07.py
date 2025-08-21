class ContaBancaria:
    def __init__ (self,titular,saldo):
        self._titular = titular
        self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, novo_titular):
        if isinstance(novo_titular, str) and novo_titular.strip() != "":
            self._titular = novo_titular
        else:
            print("Nome Inválido!")

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, novo_saldo):
        if isinstance(novo_saldo, (float)) and novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Saldo Inválido!")
