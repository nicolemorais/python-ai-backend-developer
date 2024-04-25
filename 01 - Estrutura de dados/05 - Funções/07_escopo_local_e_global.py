"""
ESCOPO DE LOCAL E GLOBAL:
- Dentro do bloco da função o escopo é local:
    - Alterações feitas em objetos imutáveis serão perdidas quando o método terminar de ser executado;
- Para usar objetos globais utilizamos a palavra-chave global:
    - Que informa ao interpretador que a variável que está sendo manipulada no escopo local é global;
    - Essa NÃO é uma boa prática e deve ser evitada (Torna a manutenção do código difícil)

"""

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500)) # 2500
