def single_number(num):
    resultado = 0

    for n in num:
        resultado ^= n
    
    return resultado

print(single_number([1,2,1,2,3,3,4,4,5,]))

