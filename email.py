def is_email(texto):
    
    if texto.count("@") != 1:
        return False

    parte1, parte2 = texto.split("@")
    if parte1 == "":
        return False
    elif "." not in parte2:
        return False
    
    elif parte2.endswith("."):
        return False
    
    elif parte2.startswith("."):
        return False

    return True


email_digitado = input("Digite um emaill: ")

resultado = is_email(email_digitado)

if resultado == True:
    print("Email válido")

else:
    print("Email inválido")