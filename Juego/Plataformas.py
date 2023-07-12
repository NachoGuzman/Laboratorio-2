import pygame

class Plataformas():
    def __init__(self, width, height, path, x, y):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




