import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
GREEN = (0,255,0)
radius = 50
while True:
     pygame.draw.circle(screen,GREEN,(100,100),radius)
     pygame.display.update()
pygame.quit()
               
