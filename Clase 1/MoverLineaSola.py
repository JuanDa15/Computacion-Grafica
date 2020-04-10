import pygame
from Library import * 
pygame.init()
witdh = 1080
reloj = pygame.time.Clock()
high = 720
window = pygame.display.set_mode([witdh,high])
end = False
counter =  True
y = 400

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
    window.fill([0,0,0])
    pygame.draw.line(window,[255,255,255],[200,y],[600,y],2)
    if counter:
        y+=1
        if y>high:
            counter = False
    else:
        y-=1
        if y<0:
            counter = True

    reloj.tick(60)
    pygame.display.flip()