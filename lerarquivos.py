texto = input("Escreva um texto: ")

with open("texto2.txt", "w") as arquivo:
    arquivo.write(texto)

with open("texto2.txt", "r") as arquivo:
    arquivo.read()

palavras = texto.split()

mais_longa = max(palavras, key=len)