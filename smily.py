def convert(s):
    s = s.replace(":)","🙂")
    s = s.replace(":(","🙁")
    return s

texto = input("Digite o texto: ")
texto_convertido = convert(texto)
print(texto_convertido)