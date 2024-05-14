class Bicicleta:
    # Atributos
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Métodos
    def buzinar(self):
        print("Plim Plim..")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Peladando rápido..")

    # def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("Azul", "Caloi", 2024, 1400)

b1.buzinar()
b1.parar()
b1.correr()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 400)
Bicicleta.buzinar(b2)
print(b2)
