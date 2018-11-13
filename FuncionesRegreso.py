# Autor: Michelle Sánchez Guerrero
# Descripción: Funciones que regresan valores

#Recibe puntos (HP 0-2505) y regresa la calificación
def calcularCalificacion(puntos):
    calificacion = 100 * puntos / 2505
    return calificacion

#Calcula los días vividos incluyendo años
def calcularDias(a, m):
    dias = a * 365
    dias = dias + m * 30
    dias = dias + a // 4
    return dias

#Función principal del algoritmo
def main():
    #hp = int(input("¿Cuántos puntos obtuviste en el examen?: "))
    #cal = calcularCalificacion(hp)
    #print("%d puntos equivalen a %.02f" % (hp, cal))

    edadA = int(input("Años enteros: "))
    edadM = int(input("Meses enteros: "))

    diasVividos = calcularDias(edadA, edadM)
    print("Has vivido %d días" % (diasVividos))

#Llama a la función principal
main()

