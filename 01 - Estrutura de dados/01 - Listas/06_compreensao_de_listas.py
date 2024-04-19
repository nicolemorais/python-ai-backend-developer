"""
Oferece uma sintaxe mais curta quando se deseja: criar uma nova lista com base nos valores de uma lista
existente (filtro)
gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.
"""

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)


quiz =  [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(quiz)