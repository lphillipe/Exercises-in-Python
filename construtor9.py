class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self. preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        if not isinstance(item, Item):
            return False
        self.itens.append(item)
        return True

c = Carrinho()
i = Item("Feijão", 10)

print(c.adicionar_item(i))
print(c.adicionar_item("texto"))
print(len(c.itens))
