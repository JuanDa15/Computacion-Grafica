import pygame
from LibreriaGeneral import *
pygame.init()

Width = 1080
High = 720
y = 400
window = pygame.display.set_mode([Width,High])
end = False
while not end:
    for event in pygame.event.get():
        #event manager
        if event.type == pygame.QUIT:
            end = True
    #graphic controller
    window.fill([0,0,0])
    pygame.draw.line(window,[255,0,0],[200,y],[600,y],2)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            y+=1
            if y > 720:
                y = 0
        elif event.key == pygame.K_UP:
            y-=1
            if y <= 0:
                y = 720
    pygame.display.flip()