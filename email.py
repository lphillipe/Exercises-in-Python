def is_mail(texto):
    texto = input("Digite um email: ")
    if "@" in texto:
        print("Tem @")
    else:
        print("Não tem @")