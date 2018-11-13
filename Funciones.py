#Autor: Michelle Sánchez Guerrero
#Ejemplos de funciones

import turtle

def main():
    print("Hola")
    print("mundo")

def dibujarCuadro(tortuga):
    tortuga.forward(100)
    tortuga.left(90)

    tortuga.forward(100)
    tortuga.left(90)

    tortuga.forward(100)
    tortuga.left(90)

    tortuga.forward(100)
    tortuga.left(90)

def dibujarFigura(tuggy):
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)
    dibujarCuadro(tuggy)
    tuggy.left(45)

#Crear una tortuga

tuggy = turtle.Turtle()
tuggy.shape("turtle")
tuggy.color("red")
tuggy.speed(0)

tuggy.left(30)

dibujarFigura(tuggy)
tuggy.color("green")
tuggy.penup()
tuggy.goto(-200,200)
tuggy.pendown()
dibujarFigura(tuggy)
tuggy.color("blue")
tuggy.penup()
tuggy.goto(200,200)
tuggy.pendown()
dibujarFigura(tuggy)
tuggy.color("orange")
tuggy.penup()
tuggy.goto(-200,-200)
tuggy.pendown()
dibujarFigura(tuggy)
tuggy.color("purple")
tuggy.penup()
tuggy.goto(200,-200)
tuggy.pendown()
dibujarFigura(tuggy)

"""
dibujarCuadro(tuggy)

tuggy.penup() #Levantar pluma
tuggy.goto(-200, -200)
tuggy.pendown() #Bajar pluma
dibujarCuadro(tuggy)

tuggy.penup() #Levantar pluma
tuggy.goto(0, -200)
tuggy.pendown() #Bajar pluma
dibujarCuadro(tuggy)

tuggy.penup() #Levantar pluma
tuggy.goto(-200, 0)
tuggy.pendown() #Bajar pluma
dibujarCuadro(tuggy)
"""



#Salir
turtle.exitonclick()