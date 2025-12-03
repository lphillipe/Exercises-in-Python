
def analisa_lista(lista):
    if not lista:
        return "A lista está vazia."
    
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    media = soma / len(lista)
    sum(1 for n in lista if n > media)

    return {
        "maior": maior,
        "menor": menor,
        "soma": soma,
        "media": media,
        "acima da media": sum(1 for n in lista if n > media)
    }

entrada = input("Digite os números separados por vírgula: ")

lista = [int(x) for x in entrada.split(",")]

resultado = analisa_lista(lista)
print("Análise da lista: ", resultado)