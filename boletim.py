def carregar_csv(arquivo):
    dados = []

    with open(arquivo, "r") as f:
        next(f)
        for linha in f:
            nome, nota = linha.strip().split(",")
            dados.append({"nome": nome, "nota": float(nota)})
        return dados

def estatisticas(dados):
    notas = [aluno["nota"] for aluno in dados]

    media = sum(notas) / len(notas)
    maior = max(dados, key=lambda x: x["nota"])
    menor = min(dados, key=lambda x: x["nota"])

    ordenados = sorted(dados, key=lambda x: x["nota"], reverse=True)

    aprovados = [aluno for aluno in dados if aluno["nota"] >= 6]
    reprovados = [aluno for aluno in dados if aluno["nota"] < 6]

    return media, maior, menor, ordenados, aprovados, reprovados

arquivo = "alunos.csv"
dados = carregar_csv(arquivo)

media, maior, menor, ordenados, aprovados, reprovados = estatisticas(dados)

print(f"\nMédia da Turma: {media:.2f}")
print(f"Maior nota: {maior['nome']} ({maior['nota']})")
print(f"Menor nota: {menor['nome']} ({menor['nota']})\n")

print("Alunos ordenados por nota:")
for aluno in ordenados:
    print(f"{aluno['nome']} ({aluno['nota']})")

print("\nAprovados")
for aluno in aprovados:
    print(f"{aluno['nome']} ({aluno['nota']})")

print("\nReprovados")
for aluno in reprovados:
    print(f"{aluno['nome']} ({aluno['nota']})")