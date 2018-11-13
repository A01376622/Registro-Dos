a = int(input("Teclea la medida a: "))
b = int(input("Teclea la medida b: "))
c = int(input("Teclea la medida c: "))
d = int(input("Teclea la medida d: "))

areaRectangulo = b * (a-c-d)
areaTrianguloizq = d * b / 2
areaTrianguloder = c * d / 2

areaTotal = areaRectangulo + areaTrianguloizq + areaTrianguloder
costo = areaTotal * 3450
pensión = 10

print(pensión)

print("Area total= ", areaTotal)
print("Costo= ", costo)