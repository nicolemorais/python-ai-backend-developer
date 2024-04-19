"""
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.
"""

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
