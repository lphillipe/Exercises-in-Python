class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dados(self):
        print(f"Voce se chama {self.nome} e seu salário é {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento