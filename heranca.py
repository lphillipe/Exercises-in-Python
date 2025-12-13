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

    def dados(self):
        super().dados()
        print(f"Departamento:{self.departamento}")


f = Funcionario("Luís", 3000)
g = Gerente("Oceana", 5000, "Pedagogia")

f.dados()
g.dados()