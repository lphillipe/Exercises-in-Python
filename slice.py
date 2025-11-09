def slices(word):
    primeiros = word[0:2] # pega posições 0 e 1
    ultimos = word[-2:]   # pega as duas últimas posições
    return primeiros, ultimos

texto = input("Palavra: ")
print(slices(texto))