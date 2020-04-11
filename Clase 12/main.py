import pygame
import random
from Player import *
from Rivales import *
from Balas import *
from LibreriaGeneral import *
#--------------------------------------------
width = 1080
high = 720
#---------------------------------------------
if __name__ == "__main__":
    #DefinicionVariables
    pygame.init()
    end = False
    reloj = pygame.time.Clock()
    window = pygame.display.set_mode([width,high])
    Player1 = Jugador()
    PlayersList = pygame.sprite.Group()
    PlayersList.add(Player1)
    Rivals = pygame.sprite.Group()
    Balas = pygame.sprite.Group()
    QuantityRivals = 10
    for i in range(QuantityRivals):
        x = 1000
        y = random.randrange(high)
        vx = -1*random.randrange(15)
        vy = 0
        r = Rival([x,y],vx,vy)
        Rivals.add(r)
        
    while not end:
        #Gestion Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Player1.velx = Player1.velx + 3
                    Player1.vely = 0
                if event.key == pygame.K_LEFT:
                    Player1.velx = Player1.velx -3
                    Player1.vely = 0
                if event.key == pygame.K_UP:
                    Player1.vely = Player1.vely - 3
                    Player1.velx = 0
                if event.key == pygame.K_DOWN:
                    Player1.vely = Player1.vely + 3
                    Player1.velx = 0
            if event.type == pygame.KEYUP:
                Player1.vely = 0
                Player1.velx = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    position = Player1.ReturnPosition()
                    bullet = PlayerBullets(position)
                    Balas.add(bullet)
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                PlayersList.update(position)
        #Control
        #Limpieza
        for b in Balas:
            if b.rect.x > (width + b.rect.w):
                Balas.remove(b)
        #Refresco
        #PlayersList.update()
        Rivals.update()
        Balas.update()
        window.fill([0,0,0])
        Rivals.draw(window)
        Balas.draw(window)
        PlayersList.draw(window)
        pygame.display.flip()
        reloj.tick(60)
