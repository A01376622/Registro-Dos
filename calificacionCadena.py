#Autor: Michelle Sánchez

def esPar(n):

    return n % 2 == 0

def clasificar(calificacion):
    if calificacion >= 70 and calificacion <= 100:
        return "Aprobado"
    else:
        if calificacion < 70 and calificacion>=0:
            return "Reprobado"

    return "Error"

def main():
    if esPar(5):
        print("Si es par")
    else:
        print("No es par")
main()