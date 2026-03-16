class Forma():

    def area(self):
        pass


class Quadrado(Forma):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    

quadrado = Quadrado(5)
area_quadrado = quadrado.area()
print(area_quadrado)

quadrado2 = Quadrado(7)
area_quadrado2 = quadrado2.area()
print(area_quadrado2)