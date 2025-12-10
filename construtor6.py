class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Loja:
    def __init__(self, nome, produtos):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        if not isinstance(produto, Produto):
            print("Isso não é um produto válido.")
            return False

        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"{produto.nome} - R$ {produto.preco}")





