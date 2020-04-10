import pygame
from Library import * 

pygame.init()
Width = 1080
High = 720
end = False
window = pygame.display.set_mode([Width,High])

while not end: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            DrawPunto(window,event.pos,event.button)