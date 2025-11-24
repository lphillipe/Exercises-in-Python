try:
    Celsius = float(input("Digite a temperatura em Celsius:"))

except ValueError:
    print("Por favor, insira um valor númerico válido")
    exit()

Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

print(f"A temperatura em Fahrenheit é:{Fahrenheit:.2f}")
print(f"A temperatura em Kelvin é:{Kelvin:.2f}")