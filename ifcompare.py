def compare_numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Digite o primeiro número:\n "))
num2 = float(input("Digite o segundo número:\n "))
num3 = float(input("Digite o terceiro número:\n "))
maior = compare_numbers(num1, num2, num3)

print("O maior número é:", maior)