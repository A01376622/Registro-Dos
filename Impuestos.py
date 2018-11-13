#Autores: Michelle Sánchez y Roberto Gonzalez
#Desripción: Programa que imprime el subtotal, el impuesto federal, el impuesto estatal, el total de los impuestos y el total de la compra.


def calcularImpuestoFederal(subtotal):
    impuestofed = subtotal * 0.17
    return impuestofed


def calcularImpuestoEstatal(subtotal):
    impuestoest = subtotal * 0.04
    return impuestoest


def calcularTotalImpuestos(subtotal):
    total = calcularImpuestoEstatal(subtotal) + calcularImpuestoFederal(subtotal)
    return total


def calcularTotalCompra(subtotal):
    compra = calcularTotalImpuestos(subtotal) + subtotal
    return compra


def imprimirResultados(subtotal, impuestofed, impuestoest, total, compra):
    print("El subtotal de la compra es: %.02f" % (subtotal))
    print("El impuesto federal es: %.02f" % (impuestofed))
    print("El impuesto estatal es: %.02f" % (impuestoest))
    print("El total de impuestos de la compra es: %.02f" % (total))
    print("El total de la compra es: %.02f" % (compra))

def imprimir(subtotal):
    calcularImpuestoFederal(subtotal)
    calcularImpuestoEstatal(subtotal)
    calcularTotalImpuestos(subtotal)
    calcularTotalCompra(subtotal)
    imprimirResultados(subtotal, impuestofed, impuestoest, total, compra)

main()