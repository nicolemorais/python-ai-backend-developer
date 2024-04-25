# Tirar uma cópia do dicionário

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

# Modidificar o valor dentro de uma chave apenas na cópia
copia["guilherme@gmail.com"] = {"nome": "Gui"}
print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
