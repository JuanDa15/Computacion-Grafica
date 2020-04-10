import pygame
import random
from LibreriaGeneral import *

width = 1080
high = 720
middle = [width/2,high/2]

class Rival(pygame.sprite.Sprite):
    def __init__(self,pos,vx,vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(SelectColor('Green'))
        self.rect = self.image.get_rect()
        position = [100,200]
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = vx
        self.vely = vy
        
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(SelectColor('White'))
        self.rect = self.image.get_rect()
        position = [100,200]
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.velx = 0
        self.vely = 0
        
    def update(self):
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        
    
if __name__ == "__main__":
    #DefinicionVariables
    pygame.init()
    end = False
    reloj = pygame.time.Clock()
    window = pygame.display.set_mode([width,high])
    j = Jugador()
    jugadores = pygame.sprite.Group()
    jugadores.add(j)
    
    rivales = pygame.sprite.Group()
    n=10
    for i in range(n):
        x = random.randrange(width)
        y = random.randrange(high)
        vx = random.randrange(10)
        vy = random.randrange(10)
        r = Rival([x,y],vx,vy)
        rivales.add(r)
        
    while not end:
        #Gestion Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    j.velx = j.velx + 1
                    j.vely = 0
                if event.key == pygame.K_LEFT:
                    j.velx = j.velx -1
                    j.vely = 0
                if event.key == pygame.K_UP:
                    j.vely = j.vely - 1
                    j.velx = 0
                if event.key == pygame.K_DOWN:
                    j.vely = j.vely + 1
                    j.velx = 0 
            if event.type == pygame.KEYUP:
                j.vely = 0
                j.velx = 0
        #Control
        #Refresco
        jugadores.update()
        rivales.update()
        window.fill([0,0,0])
        rivales.draw(window)
        jugadores.draw(window)
        pygame.display.flip()
        reloj.tick(60)