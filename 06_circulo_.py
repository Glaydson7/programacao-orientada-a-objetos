class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        import math
        return math.pi * (self.raio ** 2)


circulo = Circulo(5)
print(circulo.calcular_area())
