class Triangulo:
    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcularArea(self):
        return (self.base * self.altura) / 2

    def calcularPerimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def dibujar(self):
        print("Dibujando un triángulo con base:", self.base, "y altura:", self.altura)
