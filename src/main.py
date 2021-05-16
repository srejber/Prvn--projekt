import pygame
import sys
import random



pygame.init()

okno_sirka = 640
okno_vyska = 427

pygame.display.set_caption("První hra")
okno = pygame.display.set_mode((okno_sirka, okno_vyska))

clock = pygame.time.Clock()

icon = pygame.image.load("ufo icon.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("simulation.png")
playerX = 80
playerY = 210
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load("_Alien_.png")
enemyX = random.randint (450, 580) 
enemyY = random.randint (50, 270)
enemyX_change = 0
enemyY_change = 40

bulletImg = pygame.image.load("bullet.png")
bulletX = 640
bulletY = 0
bulletX_change = 200
bulletY_change = 0
bullet_state = "ready"


def player(x,y):
    okno.blit(playerImg, (x, y))
    
def enemy(x,y):
    okno.blit(enemyImg, (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    okno.blit(bulletImg, (x + 10, y + 16))

obraz = pygame.image.load("Back.png")
obraz = pygame.transform.scale(obraz, (okno_sirka,okno_vyska))

zap = True

while zap:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            zap = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletY = playerY
                    fire_bullet (bulletX, bulletY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
                
               
         
     okno.fill((255, 255, 255))
     okno.blit(obraz, (0,0))
     playerX += playerX_change
     playerY += playerY_change
     
     if playerY <= 0:
         playerY = 0
     elif playerY >= 370:
         playerY = 370
         
     enemyY += enemyY_change
     
     if enemyY <= 0:
         enemyY_change = 0.89
     elif enemyY >= 380:
         enemyY_change = -0.89
         
     if bulletY <= 0:
         bulletY = 200
         bullet_state = "ready" 
         
     if bullet_state is "fire":
         fire_bullet (playerX, bulletY)
         bulletX -= bulletX_change
         
     
     player(playerX,playerY)
     enemy(enemyX, enemyY)
     pygame.display.update()
     clock.tick(120)
     
else:
    pygame.quit()
    sys.exit()
