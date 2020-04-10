import pygame
from Library import *

pygame.init()
High = 720
Width = 1080
Window = pygame.display.set_mode([Width,High])
pygame.draw.line(Window,[255,0,0],[200,400],[600,400],2)
pygame.draw.line(Window,[255,0,0],[200,400],[400,250],2)
pygame.draw.line(Window,[255,0,0],[600,400],[400,250],2)
pygame.display.flip()

end = False
while not end:
    for event in pygame.event.get():
        #Controlador de eventos
        if event.type == pygame.QUIT:
            end = True
        #Controlador de Codigo
