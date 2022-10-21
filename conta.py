import datetime

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self, cliente):
        print("data abertura: {}".format(self.data_abertura))
        print("transações de {}: ".format(cliente.nome))
        for t in self.transacoes:
            print("-", t)  
            
class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito de {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True


cliente1 = Cliente('Kenya', 'Maria', '11111111111-11')
cliente2 = Cliente('Renan', 'Almeida', '222222222-22')
conta1 = Conta('123', cliente1, 1000.0)
conta2 = Conta('321', cliente2, 1000.0)
conta1.deposita(100.0)
conta1.saca(50.0)
conta1.transfere_para(conta2, 200.0)
conta1.extrato
conta1.historico.imprime(cliente1)
