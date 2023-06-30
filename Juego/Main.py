import pygame, sys
from configuraciones import *
from modo import *
from funciones import *

#dimensiones de la ventana
weight, height = 1900 , 900

#FPS
FPS = 20

#Inicializar el juego
pygame.init()

#Configuracion de la pantalla
PANTALLA = pygame.display.set_mode((weight, height))
pygame.display.set_caption("El rescate del clon")
PANTALLA.blit(fondo,(0,0))

#Reloj para los Fps
RELOJ = pygame.time.Clock()

while True:
    RELOJ.tick(FPS)

    #pygame.set_error(DEBUG)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_RIGHT] and rectangulo_personaje.x < weight - rectangulo_personaje.width):
        accion = "Derecha"
    elif(keys[pygame.K_LEFT]):
        accion = "Izquierda"
    elif(keys[pygame.K_UP]):
        accion = "Salta"
    else:
        accion = "Quieto"

    PANTALLA.blit(fondo,(0,0))
    
    actualizar_pantalla(PANTALLA, accion, lados_personaje, velocidad, lista_plataformas)

    if get_mode():
        for lado in lados_personaje:
            pygame.draw.rect(PANTALLA, "Green", lados_personaje[lado], 2)

        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Blue", lados_piso[lado], 2)

        for lado in lados_plataforma:
            pygame.draw.rect(PANTALLA, "Red", lados_plataforma[lado], 2)

    pygame.display.update()