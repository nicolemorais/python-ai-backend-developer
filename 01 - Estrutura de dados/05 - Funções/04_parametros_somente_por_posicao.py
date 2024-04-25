"""
Por padrão argumentos podem ser passados para uma função Python tanto por posição quanto explicitamente pelo nome;
Restringir a maneira de passar os argumentos melhora a legibilidade e o desempenho;
Sendo assim, precisamos apenas olhar para a definição da função para determinar se os itens são passados por:
- Posição
- Posição e nome
- Nome
"""

# Tudo o que vem antes da / é obrigatório ser passado somente por posição
# O que vier depois aceita ser nomeado normalmente
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Somente por posição antes da barra
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat",motor="1.0",combustivel="Gasolina") # válido

# Passado nomeado antes da barra
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
