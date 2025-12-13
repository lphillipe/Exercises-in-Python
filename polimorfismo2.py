from abc import ABC, abstractmethod

class Instrumento(ABC):
    
    @abstractmethod
    def tocar(self):
        pass


class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando Guitarra 🎸 ")

class Bateria(Instrumento):
    def tocar(self):
        print("Tocando Bateria 🥁")

class Piano(Instrumento):
    def tocar(self):
        print("Tocando Piano 🎹")


instrumentos = [Guitarra(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()