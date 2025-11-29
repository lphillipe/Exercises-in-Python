texto = (input(Digite uma palavra: ))
texto_limpo = texto.lower()
texto_sem_espaco = texto.replace(" ","")
invertido = texto_limpo[::-1]

if texto_limpo == invertido:
    print("É uma panlíndromo")
    return True
else:
    print("Não é um palíndromo")
    return False

return True