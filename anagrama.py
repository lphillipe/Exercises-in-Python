def anagrama(p, s):
    if len(p) != len(s):
        return False
    
    contador = {}

    for c in p:
        contador[c] = contador.get(c, 0) + 1

    for c in s:
        if c not in contador:
            return False
        contador[c] -= 1

        if contador[c] < 0:
            return False
        
    return True


print(anagrama("listen", "silent"))