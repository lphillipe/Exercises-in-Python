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