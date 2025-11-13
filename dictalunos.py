def analisar_turma():
    alunos = {}
    n = int(input("Quantos alunos? "))

    for i in range(n):
        nome = input(f"Nome do aluno {i+1}: ")
        nota = float(input("Nota: "))

        # Guarda no dicionário
        alunos[nome] = nota
    
    # Calcular média da turma
    media = sum(alunos.values()) / len(alunos)

    # Encontrar maior nota e quem tirou
    maior = max(alunos.values())
    for nome, nota in alunos.items():
        if nota == maior:
            nome_maior = nome
            break

    # Encontrar menor nota e quem tirou
    menor = min(alunos.values())
    for nome, nota in alunos.items():
        if nota == menor:
            nome_menor = nome
            break

    print(f"\nMédia da turma: {media:.2f}")
    print(f"Maior nota: {nome_maior} ({maior})")
    print(f"Menor nota: {nome_menor} ({menor})")

analisar_turma()