def count_any(dna, seq):
    cont = 0
    tamanho = len(seq)

    for i in range(len(dna) - tamanho + 1):
        if dna[i:i+tamanho] == seq:
            cont += 1
    return cont

dna = input("DNA: ")
seq = input("Sequência: ")
print(count_any(dna, seq )) 