# Criar chaves no dicionário sem vincular nenhum valor
# Criar um conjunto de chaves com valor padrão


# usando dict para dicionários que ainda não foram criados
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# Exemplo com dicionário já existente

exemplo = resultado.fromkeys(["nome", "telefone", "teste"], "completo")
print(exemplo)