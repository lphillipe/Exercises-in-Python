class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, n):
        if not isinstance(n, (int, float)):
            return False
        
        if n < 0 or n > 10:
            return False

        self.notas.append(n)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0

        soma = sum(self.notas)
        quantidade = len(self.notas)
        media = soma / quantidade
        return media


a = Aluno("João")

a.adicionar_nota(8)
a.adicionar_nota(6)
print(a.calcular_media())
