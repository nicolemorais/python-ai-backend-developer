"""
- Em python tudo é objeto incluindo funções;
- Funções são objetos de primeira classe;
- Podemos atribuir funções a variáveis, passá-las como parâmetro para funções e usá-las como valores
em estrutura de dados (listas, tuplas, dicionários, etc) e usar como valor de retorno para uma função (closures);
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação é = 20
exibir_resultado(34, 12, subtrair) # O resultado da operação é = 22

# Criar um variável para apontar para um função
op = somar
print(op(1,23))
