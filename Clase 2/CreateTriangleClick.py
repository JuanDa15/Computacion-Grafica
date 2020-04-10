import pygame
from LibreriaGeneral import *

pygame.init()
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
end = False
positions = []
verification = 0

if __name__ == "__main__":
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if verification == 0:
                    positions = event.pos
                CreateTriangleClick(window,event.pos)
                linkTriangles(window,positions,event.pos)
                positions = event.pos
                verification = 1

        