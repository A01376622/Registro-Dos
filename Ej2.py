#Autor: Michelle Sánchez
#Programa de adivina un número

import random


def main():

    numeroAleatorio = random.randint(1,10)
    print(numeroAleatorio)
    adivina = int(input("¿Cuál es el número?"))
    veces = 0

    while adivina != numeroAleatorio and veces <= 2:
        veces += 1
        print("Incorrecto, vuelve a intentarlo")


"""    
    for numeroVeces in range(0,3):

        adivina = int(input("¿Cuál es el número?"))
        if adivina == numeroAleatorio:
            print("¡Felicidades! Le atinaste al número")
        elif adivina != numeroAleatorio:
            print("Incorrecto, vuelve a intentarlo")
        else:
            print("Perdiste. El número era: ", numeroAleatorio)"""



main()