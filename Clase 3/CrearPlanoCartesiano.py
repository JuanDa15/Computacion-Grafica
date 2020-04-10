import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])

end = False

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                updateMiddle(ConvertIntList(event.pos))
                drawPlane(window,ConvertIntList(event.pos))
                