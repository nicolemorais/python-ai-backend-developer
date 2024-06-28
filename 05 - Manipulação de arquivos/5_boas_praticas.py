from pathlib import Path
from typing import TextIO

ROOT_PATH = Path(__file__).parent

# Declaração "with": Permite trabalhar com arquivos de maneira segura, garantindo que eles sejam fechados
# corretamente, mesmo em casos de exceções
try:
    with open(ROOT_PATH / "1lorem.txt", "r") as arquivo:  # -> Automatizando o processo
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

# Uso da codificação correta
# -> Certificar-se de usar a codificação correta ao ler e gravar arquivos de texto
# O argumento 'enconding' da função 'open()' permite especificar a codificação

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "w", encoding='utf-8') as arquivo:
#          arquivo.write("Aprendendo a manipular arquivos utilizando Python.")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo: {exc}")

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding='ascii') as arquivo:
#         print(arquivo.read())
# except IOError as exc:
#      print(f"Erro ao abrir o arquivo: {exc}")
# except UnicodeError as exc:
#     print(exc)

try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", "r", encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
     print(f"Erro ao abrir o arquivo: {exc}")
except UnicodeError as exc:
    print(exc)