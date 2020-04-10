import  pygame
from LibreriaGeneral import *
pygame.init()
#-----------------------------------------------------------------
width = 1080
high = 720
middle = [width/2,high/2]
window = pygame.display.set_mode([width,high])
end = False
clock = pygame.time.Clock()
angle = 0
a = 100
b = 100
#------------------------------------------------------------------
if __name__ == "__main__":
    while not end:
        drawPlane(window,middle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        p = a + (b * math.cos(math.radians(angle)))
        CartesianPosition = PolarToCartesian(p,angle)
        ScreenPosition = CartToScreen(middle,CartesianPosition)
        CreatePoint(window,ScreenPosition,[255,0,0])
        angle += 1
        clock.tick(30)