class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self. preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

c = Carrinho()

print(c.itens)