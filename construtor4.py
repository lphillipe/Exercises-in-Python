class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <=0:
            print("Valor inválido!")
        else:
            return self.saldo += valor
    
    def sacar(self, valor):
        if valor <=0:
            print("O valor não pode ser negativo.")
        elif valor > self.saldo:
            print("O valor de saque e maior que o saldo.")
        else:
            return self.saldo -= valor

    def extrato(self):
        print("Seu saldo atual é", self.saldo)

    