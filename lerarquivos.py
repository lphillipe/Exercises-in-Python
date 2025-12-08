texto = input("Escreva um texto: ")

with open("texto2.txt", "w") as arquivo:
    arquivo.write(texto)

with open("texto2.txt", "r") as arquivo:
    conteudo = arquivo.read()

linhas = conteudo.splitlines()
qtd_linhas = len(linhas)

palavras = conteudo.split()
qtd_palavras = len(palavras)

caracteres_com_espaco = len(conteudo)
caracteres_sem_espaco = len(conteudo.replace(" ", ""))

mais_longa = max(palavras, key=len)

print("Quantidades de linhas", qtd_linhas)
print("Quantidade de palavras", qtd_palavras)
print("Quantidade de caracteres com espaço", caracteres_com_espaco)
print("Quantidade de caracteres sem espaço", caracteres_sem_espaco)
print("Palavra mais longa", mais_longa)