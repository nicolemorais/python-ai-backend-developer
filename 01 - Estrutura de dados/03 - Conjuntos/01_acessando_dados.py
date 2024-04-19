"""
Conjuntos em python não suportam indexação e nem fatiamento, caso queira acessar o seus valores é necessário converter
o conjunto para lista
"""

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
