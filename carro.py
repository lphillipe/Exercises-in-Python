class Carro:
    def __init__(self, modelo, marca, preco):
        self.modelo = modelo
        self.marca = marca
        self.preco = preco

    def ligar_carro(self):
        print("Ligar carro")

    def desligar_carro(self):
        print("Desligar carro")

    def info_car(self):
        print(self.modelo, self.marca, self.preco)


c1 = Carro("Mustang", "Ford", "R$200.000")

c1.ligar_carro()
c1.desligar_carro()
c1.info_car()
