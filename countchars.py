def match_positions(a, b):
    cont = 0

    for i in range(len(a)):
        if a[i] == b[i]:
            cont += 1
    return cont

a = input("String A: ")
b = input("String B: ")
print(match_positions(a, b))