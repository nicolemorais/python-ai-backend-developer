import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

ID_COLUMN = 0
NAME_COLUMN = 1

try:
    with open(ROOT_PATH/"usuarios.csv", "w", newline='', encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Id", "Name"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "João"])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")



try:
    with open(ROOT_PATH/"usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for idx, row in enumerate(leitor):
            if idx == 0:
                continue
            print(f"ID:{row[ID_COLUMN]}")
            print(f"Name:{row[NAME_COLUMN]}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH/"usuarios.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['Id']}")
            print(f"Name: {row['Name']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
