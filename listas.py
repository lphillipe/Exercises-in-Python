def coletar_numeros():
    numeros = []

    while True:
        n = int(input("Digite um número (0 para sair): "))
        if n == 0:
            break
        numeros.append(n)
    media = sum(numeros) / len(numeros)
    return numeros, media

nums, media = coletar_numeros()
print(f"Foram digitados {len(nums)} números.")
print(f"Média: {media:.2f}")
print("Ordenados:", sorted(nums))