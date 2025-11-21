def potencia(base, expoente):
    resultado = 1
    for index in range(expoente):
        resultado = resultado * base
    return resultado

print(potencia(2, 4))