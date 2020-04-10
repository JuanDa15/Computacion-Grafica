import pygame 
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
end = False
positions = []

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                positions.append(ConvertIntList(event.pos))
                if len(positions) >= 4:
                    pygame.draw.polygon(window, [255,0,0], positions, 1)
                    pygame.display.flip()