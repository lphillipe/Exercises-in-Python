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