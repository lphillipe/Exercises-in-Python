def balanceado(s):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in '([{':
            pilha.append(c)
            
        elif c in ')]}':
            if not pilha:
                return False
            
            topo = pilha.pop()

            if topo != pares[c]:
                return False
    return len(pilha) == 0
            

    # o que a pilha vazia (ou não) significa aqui?



# Testes
print(balanceado("()[]{}"))   # True
print(balanceado("([{}])"))   # True
print(balanceado("(]"))       # False
print(balanceado("([)]"))     # False
print(balanceado("{[]"))      # False
print(balanceado(""))         # True