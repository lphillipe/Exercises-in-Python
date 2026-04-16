nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Media do aluno é {media:g} e está aprovado.")
else:
    print(f"Média do aluno é {media:g} e está reprovado.")
