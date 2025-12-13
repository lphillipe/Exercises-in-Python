class Instrumento:
    def tocar(self):
        print("Tocar Instrumento")

class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando Guitarra 🎸 ")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando Piano 🎹 ")

class Bateria(Instrumento):
    def tocar(self):
        print("Tocando Bateria 🥁")


instrumentos = [Guitarra(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()