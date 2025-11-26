try:
    contagem = int(input("Digite um número inteiro positivo: "))
    if contagem < 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        num = 0
        while num <= contagem:
            print(num)
            num += 1
        print("Contagem Crescente concluída!")


        num = contagem
        while num >= 0:
            print(num)
            num -= 1
        print("Contagem Decrescente concluída!")

        while num <= contagem:
            if num % 2 == 0:
                print(f"Números pares: {num}")
            elif num % 2 != 0:
                print(f"Números ímpares: {num}")
    

except ValueError:
    print("Digite um valor válido")
    exit()