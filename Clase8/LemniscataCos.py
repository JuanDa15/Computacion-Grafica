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
n = 5
#------------------------------------------------------------------
if __name__ == "__main__":
    while not end:
        drawPlane(window,middle)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True     
        try:
            p = math.sqrt((a*a)*math.cos(2*math.radians(angle)))
        except:
            print '.'
        CartesianPosition = PolarToCartesian(p,angle)
        ScreenPosition = CartToScreen(middle,CartesianPosition)
        CreatePoint(window,ScreenPosition,[255,0,0])
        angle += 1
        clock.tick(60)