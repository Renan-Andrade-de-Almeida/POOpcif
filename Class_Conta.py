class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo < valor:
            self.saldo -= valor
            return True
        else:
            print("Não há saldo suficiente!")
            return False

    def extrato(self):
        print("numero:{}\nsaldo:{}".format(self.numero, self.saldo))


