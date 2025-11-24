num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = float(num1) + float(num2)
    return f"O resultado da adição é: {resultado}"

elif operacao == '-':
    resultado = float(num1) - float(num2)
    return f"O resultado da subtração é: {resultado}"