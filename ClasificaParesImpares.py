#Autor: Michelle Sánchez Guerrero
#Descripción: Prueba ciclos for

def esPar(numero):
    if numero % 2 == 0:
        return True
    return False

def mostrarTabla7():
    for factor in range(1,11):
        producto = 7 * factor
        print("7 x %d = %d" % (factor, producto))

def mostrarTabla(tabla):
    print("Tabla del", tabla)
    for factor in range(1,11): #[1,10]
        producto = tabla * factor
        #print("%d x %d = %d" % (tabla, factor, producto))
        print(tabla, "x", factor, "=", producto)

def main():
    """for numero in range(1,21):
        print("%02d es " % (numero), end="")
        if esPar(numero):
            print("par")
        else:
            print("impar")"""
    #mostrarTabla7()
    for tabla in range(1,11):
        mostrarTabla(tabla)
    mostrarTabla(2.54) #Pulgadas a cm
    mostrarTabla("A")

main()