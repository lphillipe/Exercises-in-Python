def ler_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print("Entrada inválida. Por Favor, insira um número inteiro.")


def ler_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Por favor, insira um número válido (ex: 12.50).")
             
def main():
    produtos = []

    qtd = ler_int("Quantos produtos você quer cadastras? ")

    for i in range(1, qtd + 1):
        print(f"\nCadastro do produto #{i}")
        nome = input("Nome do produto: ")
        preco = ler_float("Preço (use . como separador): R$ ")
        quantidade = ler_int("Quantidade em estoque: ")

        # Monta o dicionário do produto e adiciona á lista
        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        produtos.append(produto)

        # exibe a lista completa de produtos
        print("\n=== Lista de Produtos Cadastrados ===")
        for p in produtos:
            print(f"- {p[ 'nome']}: R$ {p['preco']:.2f} (Qtde: {p['quantidade']})")

        valor_total = sum(p['preco'] * p['quantidade'] for p in produtos)
        print(f"\nValor total do estoque: R${valor_total:.2f}")

        # encontra o produto mais caro e o mais barato (pela chave 'preco')
        if produtos:
            mais_caro = max(produtos, key=lambda x: x["preco"])
            mais_barato = min(produtos, key=lambda x: x["preco"])

            print(f"Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']}")
            print(f"Produto mais barato: {mais_barato['nome']} - R$ {mais_barato['preco']}")

        else:
            print("Nenhum produto cadastrado.")


    
if __name__ == "__main__":
    main()