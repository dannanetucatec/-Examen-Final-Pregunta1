from triangulo import Triangulo

if __name__ == "__main__":
    base = 5
    altura = 3
    lado1 = 5
    lado2 = 4
    lado3 = 3

    triangulo = Triangulo(base, altura, lado1, lado2, lado3)

    print("Área del triángulo:", triangulo.calcularArea())
    print("Perímetro del triángulo:", triangulo.calcularPerimetro())
    triangulo.dibujar()
