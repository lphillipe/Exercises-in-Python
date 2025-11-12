def max_consecutive(dna, seq):
    maior = 0
    tamanho = len(seq)

    for i in range(len(dna)):
        cont = 0
        j = i

        while j + tamanho <= len(dna) and dna[j:j+tamanho] == seq:
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

dna = "AAGTAAGAAGTTTAT"
seqs = ["AAG", "TT", "AT"]

print(analyze(dna, seqs))