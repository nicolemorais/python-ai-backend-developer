"""
DESAFIO 1

# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:


# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal
# TODO: Retorne o plano de internet adequado:


# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())


# Função que retorna um verifica o consumo médio e retorna o plano recomendado:
def recomendar_plano(consumo):
    if consumo <= 10:
        plano_recomendado = "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        plano_recomendado = "Plano Prata Fibra - 100Mbps"
    else:
        plano_recomendado = "Plano Premium Fibra - 300Mbps"
    return plano_recomendado


# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

plano_recomendado = recomendar_plano(consumo)
print(plano_recomendado)
==================================================================================

DESAFIO 2

# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:

# TODO: Crie um loop para solicita os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":

itens = []


for i in range(3):
    item = input() # Entrada

    # Adiciona o tem à lista
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

=============================================================================

DESAFIO 3

"""

# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re


# TODO: Crie uma função chamada 'validate_numero_telefone' que aceite um argumento 'phone_number':
def validate_numero_telefone(phone_number):
    # TODO: Defina um padrão de expressão regular (regex) para validar números de telefone no formato (XX) 9XXXX-XXXX:
    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"

    # A função 're.match()' para verifica se o padrão definido corresponde ao número de telefone fornecido.
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
# TODO: Agora crie um return, para retornar que o número de telefone é válido:
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# TODO: Crie um else e return, caso não o número de telefone seja inválido:


# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()

# TODO: Chame a função 'validate_numero_telefone()' com o número de telefone fornecido como argumento e armazene o resultado retornado na variável 'result'.
result = validate_numero_telefone(phone_number)

# Imprime o resultado:
print(result)