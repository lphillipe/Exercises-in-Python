def contar_palavra(arquivo):
    freq = {}

    with open(arquivo, "r") as f:
        for linha in f:
            palavras = linha.lower().split()
            for p in palavras:
                freq[p] = freq.get(p, 0) + 1
    return freq

arquivo = "texto.txt"
resultado = contar_palavra(arquivo)

print("Frequência de palavras: ")
for palavra, cont in sorted(resultado.items()):
    print(palavra, ":", cont)