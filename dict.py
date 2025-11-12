def count_letters(text):
    freq = {} # dicionário vazio

    for char in text.lower():
        if char.isalpha(): # só conta letras
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
    return freq

palavra = input("Digite uma palavra: ")
resultado = count_letters(palavra)

print("Frequência: ")
for letra, cont in resultado.items():
    print(letra, ":", cont)