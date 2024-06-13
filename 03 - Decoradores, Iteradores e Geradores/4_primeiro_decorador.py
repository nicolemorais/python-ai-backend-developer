def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de excutar")
        funcao()
        print("Faz algo depois de excutar")

    return envelope


@meu_decorador
def ola_mundo():
    print("Olá mundo!")


# ola_mundo = meu_decorador(ola_mundo)

ola_mundo()
