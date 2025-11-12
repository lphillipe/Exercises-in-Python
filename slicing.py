def analisar_string(palavra):
    primeiros = palavra[:2]
    ultimos = palavra[-2:]
    invertida = palavras[::-1]
    return primeiros, ultimos, invertida

texto = input("Digite uma palavra: ")
p, u, i = analisar_string(texto)
print("Primeiros:", p)
print("Ultimos:", u)
print("Invertida", i)