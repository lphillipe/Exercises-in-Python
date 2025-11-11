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

dna = input("DNA: ")
seq = input("Sequência: ")
print(max_consecutive(dna,seq))