#Michelle
#Juego como de plants vs zombies

import pygame   # Librería de pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

#Estados
MENU = 1
JUGANDO = 2

#Estados de movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3

# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePlanta):
    ventana.blit(spritePlanta.image, spritePlanta.rect)


def dibujarFondo(ventana, fondo):
    ventana.blit(fondo, (0,0))


def dibujarZombies(ventana, listaEnemigos):
    for zombie in listaEnemigos:
        ventana.blit(zombie.image, zombie.rect)


def actualizarZombies(listaEnemigos):
    for zombie in listaEnemigos:
        zombie.rect.left -= 1


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left +=30


def verificarColisiones(listaBalas, listaEnemigos):
    #recorre las listas al revés
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        borrarBala = False

        for e in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[e]

            #Bala vs Zombie
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect

            if xb >= xe and xb <= xe + anchoe and yb <= ye and yb >= ye-altoe: #la bala está en el cuadro del enemigo
                listaEnemigos.remove(enemigo)  #borramos al enemigo (de la lista)
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Fondo
    fondo = pygame.image.load("jardin.png")

    #Personaje principal
    imgPlanta = pygame.image.load("planta1 (1).png")
    spritePlanta = pygame.sprite.Sprite() #Crear sprite vacío
    spritePlanta.image = imgPlanta #Asignar imagen
    spritePlanta.rect = imgPlanta.get_rect() #Crear lo de rect
    spritePlanta.rect.left = 0 #Eje x
    spritePlanta.rect.bottom = ALTO//2 + spritePlanta.rect.height // 2 #Eje y

    movimiento = QUIETO

    #Enemigos
    listaEnemigos = [] #Lista vacía de enemigos
    imgZombie = pygame.image.load("zombie1 (1).png")
    for zombie in range(20):
        spriteZombie = pygame.sprite.Sprite()
        spriteZombie.image = imgZombie
        spriteZombie.rect = imgZombie.get_rect()
        spriteZombie.rect.left = randint(ANCHO//2, ANCHO)
        spriteZombie.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteZombie)

    #Balas
    imgBala = pygame.image.load("bolita.jpg")
    listaBalas = []

    #Estado del juego
    estado = MENU      #Estado inicial

    #Imágenes para el menú
    imgBtnJugar = pygame.image.load("button_jugar.png")

    #Imágenes para el juego
    imgFondoJuego = pygame.image.load("pvz.png")
    xFondo = 0


    #Tiempo
    timer = 0    #acumulador de tiempo

    #Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")     #sound, es para sonidos cortos
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)


    #TEXTO
    fuente = pygame.font.SysFont("monospace", 54)



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN: #Tipo de evento, en este caso cuando se oprime una tecla
                if evento.key == pygame.K_UP: #Ver si el usuario oprimió la tecla hacia arriba
                    #spritePlanta.rect.bottom -= 15
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    #spritePlanta.rect.bottom += 15
                    movimiento = ABAJO
                elif evento.key == pygame.K_z: #disparo
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePlanta.rect.width
                    spriteBala.rect.bottom = spritePlanta.rect.bottom - 30
                    listaBalas.append(spriteBala)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2 - 12
                yb = ALTO//2-50
                anchoB = 250
                altoB = 75
                if xm>= xb and xm <= xb + anchoB and ym>= yb and ym<=yb+altoB:
                    estado = JUGANDO

        #Preguntar en qué estado está el juego
        if estado == MENU:
            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBtnJugar, (ANCHO//2-125, ALTO//2-37.5))

        elif estado == JUGANDO:
            #Actualizar objetos
            actualizarZombies(listaEnemigos)
            actualizarBalas(listaBalas)
            verificarColisiones(listaBalas, listaEnemigos)
            #Disparar????
            if timer >= 2:
                timer = 0
                efecto.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePlanta.rect.width
                spriteBala.rect.bottom = spritePlanta.rect.bottom - 30
                listaBalas.append(spriteBala)


            #Mover personaje
            if movimiento == ARRIBA:
                spritePlanta.rect.bottom -= 2
            elif movimiento == ABAJO:
                spritePlanta.rect.bottom += 2

            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgFondoJuego, (xFondo, 0))
            ventana.blit(imgFondoJuego, (xFondo + 900, 0))  #900 es el ancho de la imagen
            xFondo -= 5

            if xFondo <= -900:
                xFondo = 0

            # Dibujar, aquí haces todos los trazos que requieras
            #dibujarFondo(ventana, fondo)
            dibujarPersonaje(ventana, spritePlanta)
            dibujarZombies(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)

            #Dibujar texto
            texto = fuente.render("Tiempo: %.3f" % timer, 1, ROJO)
            ventana.blit(texto, (200, 100))   #(texto, (x,y))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/10

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()