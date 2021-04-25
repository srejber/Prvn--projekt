import pygame
import sys
import random

pygame.init()

okno_sirka = 720
okno_vyska = 480

pygame.display.set_caption("pokus o projekt")
okno = pygame.display.set_mode((okno_sirka, okno_vyska))


playerImg = pygame.image.load("ufo.png")
playerX = 150
playerY = 180
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
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
            
            

         
     okno.fill((255, 255, 255))
     okno.blit(obraz, (0,0))
     playerX += playerX_change
     playerY += playerY_change
     player(playerX,playerY)
     pygame.display.update()
else:
    pygame.quit()
    sys.exit()
