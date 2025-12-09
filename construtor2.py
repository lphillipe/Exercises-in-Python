class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def info(self):
        print(f"O seu produto é {self.nome} e seu preço é R$ {self.preco} reais")


p1 = Produto("Banana", 10)

p1.info()