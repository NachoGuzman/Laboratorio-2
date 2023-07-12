import pygame
from configuraciones import *

class Enemigos():
    def __init__(self,path, width, height, x, y, velocidad):
        self.image = reescalar_imagenes(path, width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def actualizar(self):
        self.rect.x += self.velocidad

