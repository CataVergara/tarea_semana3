import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def cambiar_radio(self, radio_nuevo):
        self.radio = radio_nuevo

circulo = Circulo(3)


print("El area del circulo es:", circulo.calcular_area())


print("El perimetro del circulo es:",circulo.calcular_perimetro())