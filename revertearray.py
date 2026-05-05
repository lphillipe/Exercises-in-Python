def reverter(arr):
    inicio = 0
    fim = len(arr) -1


    while inicio < fim:
        arr[inicio], arr[fim] = arr[fim], arr[inicio]

        inicio += 1
        fim -= 1
    
    return arr


print(reverter([2,4,5]))