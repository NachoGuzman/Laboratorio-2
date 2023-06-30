import pygame

class Plataformas():
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.image.load("Juego/background\plataforma.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

def crear_plataforma(x, y, width, height):
    plataforma = Plataformas(width, height)
    plataforma.rect.x = x
    plataforma.rect.y = y
    return plataforma