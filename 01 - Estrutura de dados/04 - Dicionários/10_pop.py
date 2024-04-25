# Remover a chave de um dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# Valor padrão caso a chave nçao exista
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
