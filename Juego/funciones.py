import pygame
from configuraciones import *
from modo import *
from Plataformas import *
from Enemigos import Enemigos

weight, height = 1900 , 900

#personaje y posicion inicial
x_inicial = height/2 - 400
y_inicial = 700

#Configuracion de imagenes
fondo = pygame.image.load("Juego/Imagenes juego/Background.jpg")
fondo = pygame.transform.scale(fondo, (weight, height))
plataforma= pygame.image.load("Juego/background\plataforma.png")
plataforma= pygame.transform.scale(plataforma, (400, 75))

#personaje
contador_pasos = 0
rectangulo_personaje = personaje_camina[0].get_rect()

#saltos
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
desplazamiento_y = 0
esta_saltando = False

#Listas
lista_animaciones = [personaje_quieto, personaje_camina, personaje_camina_izquierda, personaje_salta]

#plataformas
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 600
rectangulo_plataforma.y = 720

#fondo
fondo = pygame.image.load("Juego/Imagenes juego/Background.jpg")
fondo = pygame.transform.scale(fondo, (weight, height))

#Reescalados
reescalar_imagenes(lista_animaciones, 100, 125)

#Variables de animacion
accion = "quieto"
contador_pasos = 0

#Variables de movimiento
velocidad = 6

#Creacion del rectangulo del personaje
rectangulo_personaje = personaje_camina[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

#piso
piso = pygame.Rect(0,0, weight, 20)
piso.top = rectangulo_personaje.bottom

#Pruebas con la class Plataformas
plataforma_uno = Plataformas(400, 75, "Juego/background\plataforma.png", 1200, 760)
#plataforma_dos= Plataformas(400, 75, "Juego/background\plataforma.png", 300, 760)
#plataforma_tres= Plataformas(400, 75, "Juego/background\plataforma.png", 400, 600)

#Pruebas con la class Enemigos
#enemigo_uno= Enemigos(100,125,100, 100, 2)




def mover_personaje(rectangulo_personaje: pygame.Rect, velocidad):
    for lado in rectangulo_personaje:
        rectangulo_personaje[lado].x += velocidad

def obtener_rectangulos(principal: pygame.Rect):
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 12)
    diccionario["right"] = pygame.Rect(principal.right - 2 , principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left - 2, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 2)

    return diccionario

def animar_personaje (pantalla, rectangulo_personaje, accion_personaje):

    global contador_pasos

    largo= len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos = 0

    pantalla.blit(accion_personaje[contador_pasos], rectangulo_personaje)
    contador_pasos += 1

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, pisos: list):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje["main"], personaje_animacion)

        for lado in rectangulo_personaje:
            rectangulo_personaje[lado].y += desplazamiento_y

        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad

    for plataforma in pisos:
        if rectangulo_personaje["bottom"].colliderect(plataforma["top"]):
            esta_saltando = False
            desplazamiento_y = 0
            rectangulo_personaje["main"].bottom = plataforma["main"].top + 5
            break
        else:
            esta_saltando = True

def actualizar_pantalla(pantalla, accion,lados_personaje, velocidad, plataformas):
    global desplazamiento_y, esta_saltando


    pantalla.blit(fondo,(0,0))
    pantalla.blit(plataforma,(rectangulo_plataforma.x, rectangulo_plataforma.y))
    pantalla.blit(plataforma_uno.image, plataforma_uno.rect)
    #pantalla.blit(plataforma_dos.image, plataforma_dos.rect)
    #pantalla.blit(plataforma_tres.image, plataforma_tres.rect)


    match accion:
        case "Derecha":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje ["main"],personaje_camina)
            mover_personaje(lados_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje ["main"],personaje_camina_izquierda) 
            mover_personaje(lados_personaje, velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "Quieto":
            if not esta_saltando:
                animar_personaje(pantalla, lados_personaje ["main"], personaje_quieto)
    


    aplicar_gravedad(pantalla, personaje_salta, lados_personaje, plataformas)

lados_personaje = obtener_rectangulos(rectangulo_personaje)
lados_piso = obtener_rectangulos(piso)
lados_plataforma = obtener_rectangulos(rectangulo_plataforma)
#plataforma_uno_lados = obtener_rectangulos(plataforma_uno)

lista_plataformas = [lados_piso, lados_plataforma, plataforma_uno]



