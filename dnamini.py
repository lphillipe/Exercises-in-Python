def count_repeats(dna, seq):
    maior = 0          # guarda o maior número de repetições
    tamanho = len(seq) # tamanho da sequência

    for i in range(len(dna)):
        cont = 0
        j = i

        # enquanto o pedaço começar igual á sequência
        while dna[j:j+tamanho] == seq:
            cont += 1
            j += tamanho  # avança para checar a próxima repetição
        
        # atualiza o maior se necessário
        if cont > maior:
            maior = cont
    return maior

dna = input("DNA: ")
seq = input("Sequência: ")
print(count_repeats(dna, seq))