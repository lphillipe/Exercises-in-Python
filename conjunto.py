def ler_conjunto(mensagem):
    entrada = input(mensagem)

    lista = [x.strip() for x in entrada.split(",") if x.strip() != ""]

    numeros = [int(x) for x in lista]

    return set(numeros)


print("=== Gerenciador de Conjuntos ===")


A = ler_conjunto("Digite os números do conjunto A separados por vírgula: ")
B = ler_conjunto("Digite os números do conjunto B separados por vírgula: ")

print("\nResultados:")

uniao = A | B
print("União (A ∪ B):", sorted(uniao))

intersecao = A & B
print("Interseção (A ∩ B):", sorted(intersecao))

dif_ab = A - B
print("Diferença (A - B):", sorted(dif_ab))

dif_ba = B - A
print("Diferença (B - A):", sorted(dif_ba))


dif_sim = A ^ B
print("Diferença Simétrica: ", sorted(dif_sim))