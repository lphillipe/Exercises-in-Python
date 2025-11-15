import csv
import sys

def main():
    # 1. Verificar argumentos de linha de coamando
    if len(sys.argv) != 3:
        print("Usage: python3 dnacs50.py data.csv sequence.txt")
        sys.exit(1)

    db_filename = sys.argv[1]
    seq_filename = sys.argv[2]

    # 2 . Carregar bando de dados (CSV)
    people, strs = load_database(db_filename)

    # 3. Ler sequência de DNA (arquivo.txt)

    with open(seq_filename, "r") as f:
        dna = f.read().strip()

    # 4. Calcular contagens de cada STR na sequência de DNA
    contagens = {}
    for s in strs:
        contagens[s] = longest_match(dna, s)

    # 5. Encontrar match no banco de dados
    nome = encontrar_match(people, strs, contagens)
    print(nome)

def load_database(filename):
    people = []

    with open(filename) as f:
        reader = csv.DictReader(f)

        fieldnames = reader.fieldnames
        strs = fieldnames[1:] # Pular "name"

        for row in reader:
            person = {"name": row["name"]}
            for s in strs:
                person[s] = int(row[s])

            people.append(person)
    return people, strs

def encontrar_match(people, strs, contagens):
    for person in people:
        tudo_igual = True

        for s in strs:
            if person[s] != contagens[s]:
                tudo_igual = False
                break

        if tudo_igual:
            return person["name"]

    return "No Match"

def longest_match(sequence, subsequence):
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    # para cada posição da sequência
    for in in range(seq_len):
        count = 0

        while True:
            start = i + count * sub_len
            end = start + sub_len

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)
    return longest_run