class Conta:
    def __init__(self, tipo, numero, titular, saldo, limite) -> None:
        self.tipo = tipo
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite        

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Não há saldo suficiente!")
            return False

    def extrato(self):
        print("numero:{}\nsaldo:{}".format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            destino.deposita(valor)
            return True

contas = {}


print("<--- Inicializando Sistema --->\n   <---- Criando Conta ---->\n")

while(True):
    checaOpcao = int(input("Que tipo de conta deseja criar?\n 1 - Conta Corrente \n 2 - Conta Poupança \n\n"))
    if(checaOpcao == 1):
        contaCriada = Conta("Conta Corrente", int(input("digite o numero da conta: ")), input("digite o titular da conta: "), int(input("digite o saldo: ")), limite=50000)
        contas.update(contaCriada)
        break

print(type(contaCriada))

print(contas.keys())
        
#     elif(checaOpcao == 2):
        

# conta1 = Conta((int(input("numero da conta: "))), input("titular da conta: "), int(input("saldo: ")), limite=5000)


# while(True):
#     checaOperacao = int(input("Qual operação deseja realizar?\n 1 - Depositar \n 2 - Sacar \n 3 - transferir \n\n"))
#     if(checaOperacao == 1):
#         conta1.deposita(int(input("Quanto deseja depositar? \n")))
#         break
#     elif(checaOperacao == 2):
#         conta1.saca(int(input("Quanto deseja sacar? \n")))
#         break
#     elif(checaOperacao == 3):
#         conta2 = Conta((int(input("numero da conta: "))), input("titular da conta: "), int(input("qual o saldo da conta: ")), limite=5000)
#         conta1.transfere_para(conta2, int(input("Quanto deseja transferir? \n")))
#         break

# print("O saldo do titular {} é: ".format(conta1.titular), conta1.saldo)
# print("O saldo do titular {} é: ".format(conta2.titular),conta2.saldo)