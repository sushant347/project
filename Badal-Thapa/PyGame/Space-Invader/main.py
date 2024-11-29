import pygame
from pygame import mixer
import random
import math

pygame.init()
mixer.init()

mixer.music.load('background.wav')
mixer.music.play(-1)
screen = pygame.display.set_mode((850, 600))
pygame.display.set_caption("   Space Invader")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('bg.png')
playerimg = pygame.image.load('arcade.png')
enemyimg = pygame.image.load('enemy.png')
bulletimg = pygame.image.load('bullet.png')
enemyimg = []
enemyX = []
enemyY = []
enemyspeedX = []
enemyspeedY = []
no_of_aliens = 7

for i in range(no_of_aliens):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 786))
    enemyY.append(random.randint(30, 200))
    enemyspeedX.append(-10)
    enemyspeedY.append(40)
playerX = 425
playerY = 510
changeX = 0
check = False
bulletX = 441
bulletY = 475
score = 0 
score_font = pygame.font.SysFont('Candara', 27, 'bold')
def score_text():
    score_img = score_font.render('Score:{}'.format(score), True, 'white')
    screen.blit(score_img, (10, 10))
gameover_font = pygame.font.SysFont('Candara', 64, 'bold')
def gamover():
    gameover_img = gameover_font.render('Gamover Over', True, 'white')
    screen.blit(gameover_img, (200, 255))
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX =- 7 # playerX = playerX - changeX
            if event.key == pygame.K_RIGHT:
                changeX = 7 # playerX = playerX + changeX
            if event.key == pygame.K_SPACE:
                if check == False:
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    check = True
                    bulletX = playerX + 16
        if event.type == pygame.KEYUP:
            changeX = 0
    playerX += changeX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 785:
        playerX = 785
    for i in range(no_of_aliens):
        screen.blit(enemyimg[i], (enemyX[i], enemyY[i]))
        enemyX[i] += enemyspeedX[i]
        if enemyX[i] <= 0:
            enemyspeedX[i] = 10
            enemyY[i] += enemyspeedY[i]
        elif enemyX[i] >= 785:
            enemyspeedX[i] -= 10
            enemyY[i] += enemyspeedY[i]
        d = math.sqrt(math.pow((bulletX - enemyX[i]), 2) + math.pow((bulletY - enemyY[i]), 2))
        if d < 36:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 475
            check = False
            enemyX[i] = random.randint(0, 786)
            enemyY[i] = random.randint(30, 200)
            score += 1
        if enemyY[i] > 422:
            for j in range(no_of_aliens):
                enemyY[j] = 2000
            score_text()
            gamover()
            break
    if bulletY <= 0:
        bulletY = 473
        check = False
    if check == True:
        screen.blit(bulletimg, (bulletX, bulletY))
        bulletY -= 6
    score_text()
    screen.blit(playerimg, (playerX, playerY))
    pygame.display.update()
