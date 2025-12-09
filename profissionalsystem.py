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

def carregar_pessoas():
    pessoas = []

    try:
        with open("cadastro2.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue

                partes = linhas.split(";")
                if len(partes) !=3:
                    continue

                nome, idade_str, email = partes

                try:
                    idade = int(idade_str)

                except ValueError:
                    continue


                pessoas.append({
                    "nome": nome,
                    "idade": idade,
                    "email": email
                })
    except FileNotFoundError:
        pass

    return pessoas

def analisar_pessoas(pessoas):
    if not pessoas:
        return {
            "total": 0,
            "media_idades": 0.0,
            "emails_validos": 0,
            "mais_velhas": None
        }

    total = len(pessoas)
    soma_idades = sum(p['idade'] for p in pessoas)
    media_idades = soma_idades / total

    emails_validos = sum(1 for p in pessoas if is_email(p["email"]))
    mais_velha = max(pessoas, key=lambda p: p["idade"])

    return {
        "total": total,
        "media_idades": media_idades,
        "emails_validos": emails_validos,
        "mais_velha": mais_velhas
    }

def exibir_relatorio(stats):

    print("\n=== RELATÓRIO ===")
    print(f"Total de pessoas: {stats['total']}")
    print(f"Média das idades {stats['media_idades']:.2f}")
    print(f"E-mails válidos: {stats['emails_validos']}")

    if stats["mais_velha"] is not None:
        p = stats["mais_velha"]
        print(f"Pessoa mais velha: {p['nome']} ({p['idade']} anos)")
    else:
        print("Nenhuma pessoa cadastrada.")

def main():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar pessoas")
        print("2 - Ver relatório")
        print("0 - Sair")
        escolha = input("Opção: ").strip()

        if escolha == "1":
            cadastrar_pessoas()

        elif escolha == "2":
            pessoas = carregar_pessoas()
            stats = analisar_pessoas(pessoas)
            exibir_relatorio(stats)
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()