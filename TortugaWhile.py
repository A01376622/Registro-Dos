#Autor: Michelle Sánchez Guerrero
#Descripción: Ejemplos de ciclo while

import turtle
import random   #Números aleatorios

def main():
    ancho = turtle.Screen().window_width()
    #turtle.shape("turtle")

    turtle.Screen().bgpic("pista.png")
    turtle.Screen().addshape("tortuga.gif") #Agrega una imagen
    turtle.Screen().addshape("conejo.gif")
    turtle.Screen().addshape("correcaminos.gif")

    #2do competidor en el centro

    tortuga = turtle.Turtle()
    tortuga.shape("tortuga.gif")
    tortuga.penup()
    tortuga.goto(-ancho//2,0)
    #tortuga.pendown()

    conejo = turtle.Turtle()
    conejo.shape("conejo.gif")
    conejo.penup()
    conejo.goto(-ancho//2, ancho//4)
    #conejo.pendown()

    correcaminos = turtle.Turtle()
    correcaminos.shape("correcaminos.gif")
    correcaminos.penup()
    correcaminos.goto(-ancho//2, -ancho//4)
    #correcaminos.pendown()

    #Carrera
    meta = ancho//2-10
    while tortuga.xcor()<meta and conejo.xcor()<meta and correcaminos.xcor()<meta:
        pasosTortuga = random.randint(1,5)
        pasosConejo = random.randint(1,5)
        pasosCorrecaminos = random.randint(1,5)
        tortuga.forward(pasosTortuga)
        conejo.forward(pasosConejo)
        correcaminos.forward(pasosCorrecaminos)

    #¿quién ganó?
    if tortuga.xcor()>= conejo.xcor() and tortuga.xcor()>= correcaminos.xcor():
        print("Ganó la tortuga")
        tortuga.goto(-ancho//4,0)
        tortuga.color("white")
        tortuga.write("¡¡¡Wohoooo, gané!!!", True, "left", font=("Arial", 24, "normal"))
    elif conejo.xcor()>= tortuga.xcor() and conejo.xcor()>= correcaminos.xcor():
        print("Ganó el conejo")
        conejo.goto(-ancho//4,0)
        conejo.color("white")
        conejo.write("¡¡¡Wohoooo, gané!!!", True, "left", font=("Arial", 24, "normal"))
    else:
        print("Ganó el correcaminos")
        correcaminos.goto(-ancho//4,0)
        correcaminos.color("white")
        correcaminos.write("¡¡¡Wohoooo, gané!!!", True, "left", font=("Arial", 24, "normal"))

    """turtle.goto(-ancho//2, 0)
    turtle.left(360)

    while turtle.xcor() < ancho//2-10:
        turtle.forward(3)"""


    turtle.exitonclick()


main()