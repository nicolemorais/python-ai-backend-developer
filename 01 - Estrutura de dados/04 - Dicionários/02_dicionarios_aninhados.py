"""
- Dicionários podem armazenar qualquer tipo de objeto Python como valor
- A chave para esse valor tem que ser um objeto imutável como (strings e números)
"""
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra": {"a": 1}},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

# Acessar dicionário alinhado
extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)

