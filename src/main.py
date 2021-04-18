import pygame
import sys

pygame.init()

okno_sirka = 900
okno_vyska = 700

pygame.display.set_caption("pokus o projekt")
okno = pygame.display.set_mode((okno_sirka, okno_vyska))


rychlost = 0.25
 
w1 = 50
h1 = 50
 

x1 = (okno_sirka / 2 - w1) / 2
y1 = (okno_vyska - h1) / 2

zap = True

while zap:
     for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            zap = False
            
     stisknuto = pygame.key.get_pressed()
    
     if stisknuto[pygame.K_ESCAPE]:
         zap = False
     if stisknuto[pygame.K_LEFT]:
         x1 -= rychlost
     if stisknuto[pygame.K_RIGHT]:
         x1 += rychlost
     if stisknuto[pygame.K_UP]:
         y1 -= rychlost
     if stisknuto[pygame.K_DOWN]:
         y1 += rychlost    
     okno.fill((255, 255, 255))
     pygame.draw.rect(okno, (0, 0, 0), (x1, y1, w1, h1))
     pygame.display.update()
else:
    pygame.quit()
    sys.exit()