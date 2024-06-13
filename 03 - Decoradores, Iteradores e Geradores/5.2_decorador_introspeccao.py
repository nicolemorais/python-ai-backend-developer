import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de excutar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de excutar")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")



print(ola_mundo.__name__)
