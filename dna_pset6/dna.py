import csv

def max_consecutive(dna, seq):
    maior = 0
    tamanho = len(seq)

    for i in range(len(dna)):
        cont = 0
        j = i

        while dna[j:j+tamanho] == seq:
            cont += 1
            j += tamanho

        if cont > maior:
            maior = cont
        return maior

def analyze(dna, seqs):
    resultados = {}
    for seq in seqs:
        resultados[seq] = max_consecutive(dna, seq)

    return resultados

def load_database(arquivo_csv):
    pessoas = []

    with open(arquivo_csv, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # converter contagens de string para int

            for chave in row:
                if chave != "name":
                    row[chave] = int(row[chave])
            pessoas.append(row)
    return pessoas, reader.fieldnames[1:] # lista de STRs (exceto "name")

def carregar_sequencia(arquivo_txt):

    with open(arquivo_txt, "r") as f:
        return f.read().strip()

def encontrar_match(pessoas, contagens_str):
    for pessoa in pessoas:
        matchou = True
        for str_name, valor in contagens_str.items():
            if pessoa[str_name] != valor:
                matchou = False
                break

        if matchou:
            return pessoa["name"]
    return "No match"

def main():
    # por enquanto, hardcode: depois dá para ler de input() ou sys.argv
    banco = "small.csv"
    sequencia_arquivo = "sequence1.txt"

    pessoas, strs = load_database(banco)
    dna = carregar_sequencia(sequencia_arquivo)

    contagens = analyze(dna, strs)
    nome = encontrar_match(pessoas, contagens)
    print(nome)

if __name__ == "__main__":
    main()