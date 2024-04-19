"""
A forma mais comum para percorrer os dados de um conjunto é utilizando o comando for.
"""

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros): # enumerate (função que serve para sabermos qual é o índice dentro do laço for)
    print(f"{indice}: {carro}")
