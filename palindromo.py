def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

texto = input("Digite uma palavra ou frase:")

if eh_palindromo(texto):
    print("É um palindromo")
else:
    print("Não é um palindromo")
