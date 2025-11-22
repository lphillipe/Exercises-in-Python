
try:
    value = 10/0
    number = int(input("Digite um número:"))
    print(number)
except ValueError:
    print("Isso não é um número válido!")

except ZeroDivisionError as err:
    print(err)