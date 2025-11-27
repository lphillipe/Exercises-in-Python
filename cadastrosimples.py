

nome = input("Digite o nome da pessoa que você quer adicionar na lista: ")
idade = int(input("Digite a idade dessa pessoa: "))

open("pessoas.txt", "a") as arquivo:
arquivo.write(f"{nome}, {idade}\n")
