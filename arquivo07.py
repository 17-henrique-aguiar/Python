class ContaBancaria:
    def __init__ (self,titular,saldo):
        self._tirular = titular
        self._saldo = saldo

    def get_titu(self):
        return self._titular

    def set_titu(self, novo_titu):
        if isinstance(novo_titu, str) and novo_titu.strip() != "":
            self._titular = novo_titu
        else:
            print("Nome Inválido!")

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, novo_saldo):
        if isinstance(novo_saldo, (float)) and novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Saldo Inválido!")