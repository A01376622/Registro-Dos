# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujarCuadricula(ventana):
    DELTA = 5
    for y in range(0, ALTO, DELTA):
        pygame.draw.line(ventana, ROJO, (0, y), (ANCHO, y))

    #Líneas verticales
    for x in range(0, ANCHO, DELTA):
        pygame.draw.line(ventana, ROJO, (x, 0), (x, ALTO))

def dibujarCirculos(ventana):


    for radio in range(10, ALTO//2+1, 10):
        pygame.draw.circle(ventana , AZUL, (ANCHO//2, ALTO//2), radio, 1)


def dibujarCuadrados(ventana):

    for delta in range (10, ALTO//2, 10):
        pygame.draw.rect(ventana, VERDE_BANDERA, (ANCHO//2 - delta, ALTO//2 - delta, 2*delta, 2*delta), 1)

#def prueba(ventana):
 #   for y in range (0, ALTO, 10):
  #      pygame.draw.line()
"""def dibujarParabola(ventana):

    for y in range (ALTO//2, ALTO, 10):
        pygame.draw.line(ventana, ROJO, (ALTO//2, y), (ANCHO, y))
    for x in ranfe (0, ANCHO//2, 10):"""

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variabel termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        #dibujarCuadricula(ventana)
        dibujarCirculos(ventana)
        dibujarCuadrados(ventana)
        #dibujarParabola()

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()
    #dibujarCuadricula()# Por ahora, solo dibuja


# Llamas a la función principal
main()