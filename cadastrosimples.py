

nome = input("Digite o nome da pessoa que você quer adicionar na lista: ")
idade = int(input("Digite a idade dessa pessoa: "))

with open("pessoas.txt", "a").write(f"{nome}, {idade}\n")

with open("pessoas.txt", "r") as arquivo:
    print("Lista de pessoas cadastradas:")
    for linha in arquivo:
        print(linha.strip())

