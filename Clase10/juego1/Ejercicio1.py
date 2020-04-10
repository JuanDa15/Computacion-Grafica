import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
reloj = pygame.time.Clock()
window = pygame.display.set_mode([width,high])
end = False
posx = 100
posy = 100
velx = 0
vely = 0

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velx-=1
                    vely = 0
                if event.key == pygame.K_RIGHT:
                    velx += 3
                    vely = 0
                if event.key == pygame.K_SPACE:
                    velx = 0
                    vely = 0
                if event.key == pygame.K_UP:
                    vely-= 1
                    velx = 0
                if event.key == pygame.K_DOWN:
                    vely += 1
                    velx = 0
        #Control de limites
        if posx > (width-32):
            posx = 0
        if posx < 0:
            posx = width-32
        if posy < 0:
            posy = high-32
        if posy > (high - 32):
            posy = 0
        window.fill([0,0,0])
        #Background = pygame.image.load('C:\Users\Jdoo1\Documents\Computacion Grafica\Clase10\juego1\Background.png')
        #window.blit(Background,[0,0])
        pelota = pygame.image.load('C:\Users\Jdoo1\Documents\Compugrafica\Computacion Grafica\Clase10\juego1\pelota.png')
        print pelota.get_rect()
        window.blit(pelota,[posx,posy])
        posx += velx
        posy += vely
        pygame.display.flip()
        reloj.tick(120)
        
        
