class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def maior_de_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False


p1 = Pessoa("Luís", 30)
p2 = Pessoa("Oceana", 29)
p3 = Pessoa("Saria", 8)

pessoas = [p1, p2, p3]

for pessoa in pessoas:
    if pessoa.maior_de_idade():
        print("Sim, é maior de idade.")
    else:
        print("Não é maior de idade.")