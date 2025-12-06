class Produtos:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def adicionar(self, qtd):
        if qtd > 0:
            self.quantidade += qtd
            print(f"{qtd} unidades adicionadas. Novo estoque: {self.quantidade}")

        else:
            print("Quantidade inválida. Use apenas valores positivos.")

    def remover(self, qtd):
        if qtd <= 0:
            print("Quantidade inválida. Informe um valor positivo.")
            return

        if qtd > self.quantidade:
            print(f"Não é possível remover {qtd} unidades. Estoque atual: {self.quantidade}.")
            return

        self.quantidade -= qtd
        print(f"{qtd} unidades removidas. Estoque restante: {self.quantidade}.")


p1 = Produtos("Banana",10.0, 12)
p2 = Produtos("Melancia", 5.0, 1)
p3 = Produtos("Melão", 10.0, 1)

produtos = [p1, p2, p3]

for produto in produtos:
    print(produto.nome, produto.valor_total())

total_estoque = sum(p.valor_total() for p in produtos)
print("Valor total do estoque é: ", total_estoque)


def testar_produtos():
    print("=== Testando Produtos ===")
    print("\n--- Testando valor_total() ---")
    print(p1.valor_total())
    print(p2.valor_total())
    print(p3.valor_total())
    print("\n--- Testando adicionar() ---")
    p1.adicionar(5)
    p1.adicionar(0)
    p1.adicionar(-2)

    print("\n--- Testando remover() ---")
    p1.remover(3)
    p2.remover(10)
    p3.remover(0)
    p3.remover(-5)
    p3.remover(1)  # Remoção válida

    print("=== Fim dos testes ===")
testar_produtos()