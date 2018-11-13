#Autor: Michelle Sánchez Guerrero
#Dibuja un triángulo dada la altura y también área y perímetro
#Ejemplo de diseño Top-Down

import math
import turtle

def calcularLado(altura):
    lado = altura / math.cos(math.radians(30))
    return lado

def dibujarTriangulo(lado):
    tortuga = turtle.Turtle()  # Crea una tortuga
    tortuga.shape("turtle")
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.forward(lado)
    tortuga.left(120)
    turtle.exitonclick()

def dibujar(altura):
    lado = calcularLado(altura)
    dibujarTriangulo(lado)

def calcularArea(altura):
    base = calcularLado(altura)
    area = (base * altura) / 2
    return area

def calcularPerimetro(altura):
    perimetro = calcularLado(altura) * 3
    return perimetro


def imprimirResultados(area, perimetro):
    print("Area = %.2f" %(area))
    print("Perímetro = %.2f" % (perimetro))


def imprimir(altura):
    area = calcularArea(altura)
    perimetro = calcularPerimetro(altura)
    imprimirResultados(area, perimetro)

def main():
    altura = int(input("Teclea la altura del triángulo: "))
    imprimir(altura)
    dibujar(altura)



#Llamamos a la función main
main()