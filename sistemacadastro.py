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

pessoas = []

with open("cadastro.txt", "r", encoding="utf-8") as arq:
    for linha in arq:
        linha = linha.strip()
        if not linha:
            continue
        nome, idade_str, email = linha.split(";")
        idade = int(idade_str)

        pessoas.append({
            "nome": nome,
            "idade": idade,
            "email": email
        })

total_pessoas = len(pessoas)

soma_idades = sum(p["idade"] for p in pessoas)

media_idades = soma_idades / total_pessoas

email_validos = sum(1 for p in pessoas if is_email(p["email"]))

mais_velha = max(pessoas, key=lambda p: p["idade"])

print(f"Total de pessoas: {total_pessoas}")
print(f"Média de idades: {media_idades:.2f}")
print(f"Quantidade de emails válidos: {email_validos}")
print(f"Pessoa mais velha: {mais_velha['nome']} ({mais_velha['idade']} anos)")
 