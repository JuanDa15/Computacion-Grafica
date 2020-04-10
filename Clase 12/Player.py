import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('C:\Users\Jdoo1\Documents\Compugrafica\Computacion Grafica\Clase 12\Pelota Jugador.png')
        self.rect = self.image.get_rect()
        position = [100,200]
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely