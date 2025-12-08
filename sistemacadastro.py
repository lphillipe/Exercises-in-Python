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


while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")

    if not is_email(email):
        print("Email inválido! Tente novamente\n")
        continue
    
    with open("cadastro.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{nome};{idade};{email}\n")

    continuar = input("Deseja cadastrar outro usuário? ").strip().lower()

    if continuar != "s":
        break






