import pygame
import sys
import random

pygame.init()

okno_sirka = 720
okno_vyska = 480

pygame.display.set_caption("První hra")
okno = pygame.display.set_mode((okno_sirka, okno_vyska))

icon = pygame.image.load("ufo icon.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("ufo.png")
playerX = 130
playerY = 210
playerX_change = 0
playerY_change = 0


def player(x,y):
    okno.blit(playerImg, (x, y))

obraz = pygame.image.load("background.png")
obraz = pygame.transform.scale(obraz, (okno_sirka,okno_vyska))

zap = True

while zap:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            zap = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            
            

         
     okno.fill((255, 255, 255))
     okno.blit(obraz, (0,0))
     playerX += playerX_change
     playerY += playerY_change
     
     if playerY <= 0:
         playerY = 0
     elif playerY >= 420:
         playerY = 420
     
     player(playerX,playerY)
     pygame.display.update()
else:
    pygame.quit()
    sys.exit()
