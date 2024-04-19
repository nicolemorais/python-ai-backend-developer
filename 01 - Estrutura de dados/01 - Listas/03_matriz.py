"""
Lista aninhadas (Matriz)
Podem armazenar todos os tipos de objetos
É possível criar estruturas bidimensionais (tabelas) - Acessar informando índices de linha e coluna.
"""

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
