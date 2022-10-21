import datetime

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-", t)  
            
class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=10000):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self):
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True


c1 = Conta('123-4', 'João', 120.0, 1000.0) 
c2 = c1 
print(c2.saldo)
#120.0
c1.deposita(100.0) 
print(c1.saldo) 
#220.0 
c2.deposita(30.0) 
print(c2.saldo)
#250.0 
print(c1.saldo) 
#250.0