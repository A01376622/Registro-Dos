#Autor: Michelle
#Descripción: calcular la aproximación de PI


def aproximacionValorPI(terminos):
    suma = 0 #Acumulador

    for denominador in range(1, terminos+1):
        suma += 1/(denominador**2)

    return (6*suma)**0.5


def main():
    terminos = int(input("Teclea cuantos números quieres"))
    aproximacionPI = aproximacionValorPI(terminos)
    print("PI =", aproximacionPI)


main()