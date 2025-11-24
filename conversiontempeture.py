try:
    Celsius = float(input("Digite a temperatura em Celsius:"))

except:
    print("Por favor, insira um valor númerico válido")
    exit()

Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15

print("A temperatura em Fahrenheit é:", Fahrenheit)
print("A temperatura em Kelvin é:", Kelvin)