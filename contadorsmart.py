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

        while num >= 0:
            print(num)
            num -= 1
        print("Contagem Decrescente concluída!")
    

except ValueError:
    print("Digite um valor válido")
    exit()