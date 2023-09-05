class Rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcular_area(self):
        return self.longitud * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.longitud + self.ancho)

    def cambiar_longitud(self, nueva_longitud):
        self.longitud = nueva_longitud

    def cambiar_ancho(self, nuevo_ancho):
        self.ancho = nuevo_ancho


rectangulo = Rectangulo(8, 4)


print("el area del perimetro es:", rectangulo.calcular_area())


print("el perimetro del rectangulo es:", rectangulo.calcular_perimetro())
