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

def estatisticas(dados):
    notas =[aluno["nota"] for aluno in dados]

    media = sum(notas) / len(notas)

    maior_aluno = max(dados, key=lambda x: x["nota"])
    menor_aluno = min(dados, key=lambda x: x["nota"])

    return media, maior_aluno, menor_aluno

arquivo = "alunos.csv"
dados = carregar_csv(arquivo)

resultado = estatisticas(dados)

media = resultado[0]
maior_aluno = resultado[1]
menor_aluno = resultado[2]

print("Média:", media)
print("Maior:", maior_aluno["nome"], "(", maior_aluno["nota"], ")")
print("Menor:", menor_aluno["nome"], "(", menor_aluno["nota"], ")")