def is_mail(texto):
    if "@" in texto and "." in texto:
        return True
    else:
        return False


email_digitado = input("Digite um emaill: ")

resultado = is_mail(email_digitado)

if resultado == True:
    print("Email válido")

else:
    print("Email inválido")