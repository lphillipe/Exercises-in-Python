def readability(texto):
    letras = 0
    frases = 0

    # Contar letras e frases
    for char in texto:
        if char.isalpha():
            letras += 1
        if char in ".!?":
            frases += 1
    
    # contar palavras
    palavras = len(texto.split())

    # calcular L e S

    L = letras / palavras * 100
    S = frases / palavras * 100

    # Coleman-Liau
    grade = 0.0588 * L - 0.296 * S - 15.8

    # Condições finais

    if grade < 1:
        return "Before Grade 1"
    elif grade >= 16:
        return "Grade 16+"
    else:
        return f"Grade {round(grade)}"

texto = input("Texto: ")
print(readability(texto))