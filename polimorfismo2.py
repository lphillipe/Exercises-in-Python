from abc import ABC, abstractmethod

class Instrumento(ABC):
    
    @abstractmethod
    def tocar(self):
        pass


i = Instrumento()