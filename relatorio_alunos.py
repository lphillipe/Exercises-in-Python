def carregar_csv(arquivo):
    dados = []

    with open(arquivo, "r") as f:
        next(f) # pular cabeçalho

        for linha in f:
            linha = linha.strip()
            nome, nota = linha.split(",")
            nota = float(nota)
            dados.append({"nome": nome, "nota": nota})

    return dados

def estatiticas(dados):
    notas = [aluno["nota"] for aluno in dados]

    media = sum(notas) / len(notas)
    maior = max(dados, key=lambda x: x["nota"])
    menor = min(dados, key=lambda x: x["nota"])

    return media, maior, menor

def gerar_relatorio(dados, arquivo_saida, corte=6.0):
    media, maior, menor = estatiticas(dados)

    # ordenar por nota (decrescente)
    ordenados = sorted(dados, key=lambda x: x["nota"], reverse=True)

    aprovados = [aluno for aluno in dados if aluno["nota"] >= corte]
    reprovados = [aluno for aluno in dados if aluno["nota"] < corte]


    with open(arquivo_saida, "w") as f:
        f.write(f"Média da Turma: {media:.2f}\n")
        f.write(f"Maior nota: {maior['nome']} ({maior['nota']:.1f})\n")
        f.write(f"Menor nota: {menor['nome']} ({menor['nota']:.1f})\n")

        f.write("Alunos ordenados por nota:\n")
        for aluno in ordenados:
            f.write(f"{aluno['nome']} ({aluno['nota']:.1f})\n")

        f.write("\nAprovados\n")
        for aluno in aprovados:
            f.write(f"{aluno['nome']} ({aluno['nota']:.1f})\n")

        f.write("\nReprovados\n")
        for aluno in reprovados:
            f.write(f"{aluno['nome']} ({aluno['nota']:.1f})\n")

arquivo = "alunos.csv"
dados = carregar_csv(arquivo)

gerar_relatorio(dados, "relatorio.txt")
print("Relatório salvo em relatorio.txt")