def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de excutar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de excutar")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo('João')
ola_mundo(resultado)
print(ola_mundo.__name__)
