# Segunda forma de acessar valores dentro do dicionário
# Get verifica se um dicionário existe

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# Caso não exista o dicionário
resultado = contatos.get("chave")  # None
print(resultado)

# Definir um valor padrão caso o dicionário não exista
resultado = contatos.get("chave", {})  # {}
print(resultado)


resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
