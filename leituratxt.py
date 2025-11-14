def analisar_arquivo(nome):
    linhas = 0
    palavras = 0
    caracteres = 0

    with open(nome, "r") as f:
        for linha in f:
            linhas += 1
            caracteres += len(linha)
            palavras += len(linha.split())
    return linhas, palavras, caracteres


arquivo = "input.txt"
resultado = analisar_arquivo(arquivo)

print("Linhas:", resultado[0])
print("Palavras:", resultado[1])
print("Caracteres:", resultado[2])