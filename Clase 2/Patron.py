import pygame
import math
from LibreriaGeneral import *

pygame.init()
width = 666
high = 300
window = pygame.display.set_mode([width,high])
end = False
patron = 0
xposition = 0
sideLenght = 15

if __name__ == "__main__":
    xposition = math.floor(15/2)
    distance = xposition
    
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True                        
        while xposition < (width - distance):
                drawPatron(window,high,xposition)
                xposition = (xposition + (15)) + distance