#Michelle Sánchez Guerrero
#Programa

def voltearNumeros(numero):

    contador = 0
    digitos = 0

    while numero >= 1:
        numero = numero//10
        digitos += 1
    print(digitos)

    while numero//10 != 0:

        for coeficiente in range(digitos, 1, -1):
            residuo = numero % 10
            contador += residuo * coeficiente
            numero = numero //10
        print(contador)




def main():
    numero = int(input("Qué número quieres"))
    voltearNumeros(numero)


main()