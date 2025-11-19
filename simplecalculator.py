num1 = int(input("Digite o primeiro número:\n "))
op = input("Digite a operação (+, -, *, /):\n ")
num2 = int(input("Digite o segundo número:\n "))

if op == "+":
    print("Resultado:", num1 + num2)
elif op == "-":
    print("Resultado:", num1 - num2)
elif op == "*":
    print("Resultado:", num1 *num2)
elif op == "/":
    print("Resultado:", num1 / num2)
else:
    print("Operação inválida!")