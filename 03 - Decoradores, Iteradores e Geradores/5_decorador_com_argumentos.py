
def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de excutar")
        funcao(*args, **kwargs)
        print("Faz algo depois de excutar")

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")


ola_mundo('João')