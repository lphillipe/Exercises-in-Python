def contar_letras(palavra):
    vogais = "aeiouAEIOU"
    cont_vogais = 0
    cont_consoantes = 0

    for char in palavra:
        if char.isalpha(): # so letras
            if char in vogais:
                cont_vogais += 1
            else:
                cont_consoantes += 1
    return cont_vogais, cont_consoantes

texto = input("Digite uma palavra: ")
v, c = contar_letras(texto)
print("Vogais:", v)
print("Consoantes", c)