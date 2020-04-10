import pygame
import math
from LibreriaGeneral import *
pygame.init()
TriangleLenght = 500
pointA = [290,520]
pointB = [790,520]
pointC = [540,20]
index = 0
index1 = 0
index2 = 0
width = 1080
high = 720
window = pygame.display.set_mode([width,high])
end = False


if __name__ == "__main__":
    cantDivisions = TriangleLenght/50
    ymov = TriangleLenght/10
    xmov  = (TriangleLenght/2)/10
      
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
                
        while index <= cantDivisions:
            createLine(window,pointA,pointC,[0,0,255]) 
            pointA[0] = pointA[0] + 50
            index += 1

        pointA = [290,520] 
        
        while index1 <= cantDivisions:
            createLine(window,pointA,pointB,[0,255,0])
            pointB[0] = pointB[0] - xmov
            pointB[1] = pointB[1] - ymov
            index1 += 1
        
        pointB = [790,520]
        
        while index2 <= cantDivisions:
            createLine(window,pointB,pointA,[255,0,0])
            pointA[0] = pointA[0] + xmov
            pointA[1] = pointA[1] - ymov
            index2 += 1