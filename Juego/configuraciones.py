import pygame


def girar_imagenes(lista_original, flip_x, flip_y):
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    
    return lista_girada

def reescalar_imagenes(lista_animaciones, W, H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (W, H))
    
personaje_camina = [
    pygame.image.load("Juego\Movimiento personaje principal\91.png"),
    pygame.image.load("Juego\Movimiento personaje principal\92.png"),
    pygame.image.load("Juego\Movimiento personaje principal\93.png"),
    pygame.image.load("Juego\Movimiento personaje principal\94.png"),
    pygame.image.load("Juego\Movimiento personaje principal\95.png"),
    pygame.image.load("Juego\Movimiento personaje principal\96.png"),
    pygame.image.load("Juego\Movimiento personaje principal\97.png"),
    pygame.image.load("Juego\Movimiento personaje principal\98.png"),
]

personaje_quieto = [

    pygame.image.load("Juego\Movimiento personaje principal/54.png")
]

personaje_salta = [
    pygame.image.load("Juego\Movimiento personaje principal/139.png")
]

enemigo_camina = [
    pygame.image.load("Juego\Movimiento personaje principal\91.png"),
    pygame.image.load("Juego\Movimiento personaje principal\92.png"),
    pygame.image.load("Juego\Movimiento personaje principal\93.png"),
    pygame.image.load("Juego\Movimiento personaje principal\94.png"),
    pygame.image.load("Juego\Movimiento personaje principal\95.png"),
    pygame.image.load("Juego\Movimiento personaje principal\96.png"),
    pygame.image.load("Juego\Movimiento personaje principal\97.png"),
    pygame.image.load("Juego\Movimiento personaje principal\98.png"),
]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
enemigo_camina_izquierda = girar_imagenes(enemigo_camina, True, False)



