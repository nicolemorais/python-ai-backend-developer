"""
Set = É uma coleção de objetos que tem elementos únicos (sem estar duplicados)
Sets podem ser usados para representar conjuntos matemáticos ou eliminar itens de um iterável
Não confiar na ordem que set irá retornar
"""

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)
