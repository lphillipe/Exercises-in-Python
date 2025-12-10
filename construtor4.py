class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo if saldo >= 0 else 0

    def depositar(self, valor):
        if valor <=0:
            print("Valor inválido")
            return False
        self.saldo += valor
        print(f"Deposito de {valor:.2f} concluído")
        return True
    
    def sacar(self, valor):
        if valor <=0:
            print("Valor não pode ser negativo")
            return False
        if valor > self.saldo:
            print("Valor não pode ser maior que o saldo")
            return False
        self.saldo -= valor
        print(f"Saque de R$ {self.saldo:.2f} efetuado com sucesso")
        return True

    def extrato(self):
        print(f"Seu saldo atual é: R$ {self.saldo:.2f}")
        return self.saldo


c = Conta("Luís", 3100)

c.depositar(500)
c.sacar(1000)
c.extrato()
    