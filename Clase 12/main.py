import pygame
import random
from Player import *
from Rivales import *
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
    QuantityRivals = 5
    for i in range(QuantityRivals):
        x = 900
        y = random.randrange(high)
        vx = -1*random.randrange(10)
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
        #Control
        #Refresco
        PlayersList.update()
        Rivals.update()
        window.fill([0,0,0])
        Rivals.draw(window)
        PlayersList.draw(window)
        pygame.display.flip()
        reloj.tick(60)
