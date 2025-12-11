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
    
    def total(self):
        return sum(i.preco for i in self.itens)

c = Carrinho()
c.adicionar_item(Item("Oleo", 10))
c.adicionar_item(Item("Macarrão", 5))
print(c.total())
