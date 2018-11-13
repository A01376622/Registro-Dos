#Autor: Michelle Sánchez
#Programa que determina si un triángulo rectángulo

def determinarhip(a, b, c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c

def determinartriangulorectangulo(a, b, c):
    rect = True
    catetos = a**2 + b**2
    if catetos == c**2:
        return rect
    else:
        rect = False
        return rect

def main():
    ladoA = int(input("Introduzca cuanto vale el primer lado: "))
    ladoB = int(input("Introduzca cuanto vale el segundo lado: "))
    ladoC = int(input("Introduzca cuanto vale el tercer lado: "))
    hipotenusa = determinarhip(ladoA, ladoB, ladoC)
    triangulorect = determinartriangulorectangulo(ladoA, ladoB, hipotenusa)
    print("El triangulo es", triangulorect)

main()

