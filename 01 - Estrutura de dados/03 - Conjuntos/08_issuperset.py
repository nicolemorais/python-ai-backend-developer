conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# (Se um conjunto é um subconjunto de outro, todos os elementos de  B estão em A)
resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

# Todos os elementos de A estão em B
resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
