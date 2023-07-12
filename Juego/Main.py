import pygame, sys
from modo import *
from funciones import *
from GUI_form_prueba import FormPrueba

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

#from_prueba = FormPrueba(PANTALLA, 0, 0, 1000, 700, "gold", "Magenta", 5, True)

while True:
    RELOJ.tick(FPS)


    eventos = pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed()

    if(keys[pygame.K_RIGHT] and rectangulo_personaje.x < weight - rectangulo_personaje.width):
        accion = "Derecha"
    elif(keys[pygame.K_LEFT] and rectangulo_personaje.x > 0):
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
            



    #from_prueba.update(eventos)

    pygame.display.update()