def busca_binaria(nums, alvo):
    esquerda = 0
    direita = len(nums) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if nums[meio] == alvo:
            return meio
        elif nums[meio] < alvo:
            esquerda = meio + 1

        else:
            direita = meio - 1
    return -1


print(busca_binaria([1,3,5,7,9,11], 7))