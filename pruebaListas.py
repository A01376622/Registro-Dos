#Autor: Michelle Sánchez Guerrero
#Descripción: prueba de listas

def main():
    datos = [] #Lista vacía
    numero = int(input("Valor: [-1 termina] "))
    while numero != -1:
        datos.append(numero)
        numero = int(input("Valor: [-1 termina] "))

    print("Datos capturados: ", datos)
    print("Número de datos: ", len(datos))

    if len(datos) > 0:
        print("Mayor: ", max(datos))
        print("Menor: ", min(datos))
        promedio = sum(datos)/len(datos)
        print("Promedio: ", promedio)
        for k in range(len(datos)-1, -1, -1):
            print(datos[k])
        print("Doble")
        for k in range(len(datos)):
            print(2*datos[k])
    else:
        print("no hay datos")

main()