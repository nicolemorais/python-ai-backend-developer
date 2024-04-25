# Outra forma de remover valores

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remove apenas o valor telefone
del contatos["guilherme@gmail.com"]["telefone"]
# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)

# Remove o dicionário inteiro
del contatos["chappie@gmail.com"]

resultado = contatos.get("chappie@gmail.com", "não existe")
print(resultado)

# Apagar o dicionário por completo
# del contatos


