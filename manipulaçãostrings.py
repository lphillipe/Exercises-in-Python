frase = input("Digite uma frase: ")

quantidade_palavras = len(frase.split())

vogais = "aeiou"
contador_vogais = 0

for letra in frase.lower():
    if letra in vogais:
        contador vogais += 1

frase_invertida = frase[::-1]

frase_upper = frase.upper()

frase_sem_espaco = frase.replace(" ", "")

print("Número de palavras: \n", quantidade_palavras)
print("Número de vogais: \n", contador_vogais)
print("Frase invertida: \n", frase_invertida)
print("Frase em maiúsculas: \n", frase_upper)
print("Frase sem espaços: \n", frase)
