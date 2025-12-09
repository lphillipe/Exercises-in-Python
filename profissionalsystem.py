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


def cadastrar_pessoas():
    while True:
        nome = input("Nome: ").strip()

        while True:
            idade_input = input("Idade: ").strip()
            try:
                idade = int(idade_input)
                if idade < 0:
                    print("Idade não pode ser negativa. Tente novamente!")
                    continue
                break
            except ValueError:
                print("Idade inválida. Digite um número inteiro.")

        email = input("Email: ").strip()

        if not is_email(email):
            print("Email inválido! Tente novamente\n")
            continue
    
        with open("cadastro2.txt", "a", encoding="utf-8") as arq:
            arq.write(f"{nome};{idade};{email}\n")

        continuar = input("Deseja cadastrar outro usuário? (s/n): ").strip().lower()

        if continuar != "s":
            break

cadastrar_pessoas()

if __name__ == "__main__":
    cadastrar_pessoas()