def traducao(frase):
    traducao_frase = ""

    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                traducao_frase = traducao_frase + "G"
            else:
                traducao_frase = traducao_frase + "g"
        else:
            traducao_frase = traducao_frase + letra
    return traducao_frase
print(traducao(input("Digite uma palavra: ")))
