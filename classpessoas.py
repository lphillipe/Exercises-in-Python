class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_de_idade(self):
        return self.idade >= 18


p1 = Pessoa("Luís", 30)
p2 = Pessoa("Oceana", 29)
p3 = Pessoa("Saria", 8)

pessoas = [p1, p2, p3]

for pessoa in pessoas:
    if pessoa.maior_de_idade():
        print(f"Sim, {pessoa.nome} é maior de idade.")
    else:
        print(f"{pessoa.nome}, não é maior de idade.")