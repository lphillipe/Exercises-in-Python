def single_number(num):
    contador = {}

    for n in num:
        contador[n] = contador.get(n, 0) + 1

    for n in contador:
        if contador[n] == 1:
            return n
        

print(single_number([1,1,2,2,3,4,4]))