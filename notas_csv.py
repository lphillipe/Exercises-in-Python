def carregar_csv(arquivo):
    dados = []

    with open(arquivo, "r") as f:
        next(f) # pular cabeçalho
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue # pula linhas vazias
            
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

def salvar_aprovados(dados, arquivo_saida, corte=6.0):
    with open(arquivo_saida, "w") as f:
        f.write("nome, nota\n")
        
        for aluno in dados:
            if aluno["nota"] >= corte:
                f.write(f"{aluno['nome']},{aluno['nota']}\n")

arquivo = "alunos.csv"
dados = carregar_csv(arquivo)

media, maior, menor = estatiticas(dados)

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior['nome']} ({maior['nota']})")
print(f"Menor nota: {menor['nome']}({menor['nota']})")

salvar_aprovados(dados, "aprovados.csv")
print("Arquivo aprovados.csv gerado.")