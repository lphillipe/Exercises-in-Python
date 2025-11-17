frase = "Luís Phillipe você é foda e capaz de tudo!!"

print(frase.upper()) # deixa tudo em maisuculo

print(len(frase)) # conta quantos caracteres tem a frase

print(frase[2])
print(frase.index("L"))
print(frase.replace("Luís", ("Oceana")))


lucky_numbers = [42, 10, 35, 4, 16, 1]
friends = ["Luís","Kevin", "Francisco", "Marcela", "Joaquina"]
friends.extend(lucky_numbers)
print(friends)