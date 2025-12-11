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

    def listar_items(self):
        return [f"{i.nome} - R$ {i.preco:.2f}" for i in self.itens]

# --- Testes rápidos ---
if __name__ == "__main__":
    c = Carrinho()
    c.adicionar_item(Item("Arroz", 20))
    c.adicionar_item(Item("Óleo", 7.5))
    c.adicionar_item("não é item")  # será ignorado/retorna False

    print("Itens no carrinho:")
    print("\n".join(c.listar_items()))
    print("Total: R$", f"{c.total():.2f}")
