class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        novo = Node(val)
        if not self.head:
            self.head = novo
            return
        atual = self.head
        while atual.next:
            atual = atual.next
        atual.next = novo

    def contar(self):
        contador = 0
        atual = self.head

        while atual:
            contador +=1
            atual = atual.next

        return contador
    

ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(5)
ll.append(7)
print(ll.contar())