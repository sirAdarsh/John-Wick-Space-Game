import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("John Wick 4")

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
gunImg = pygame.image.load('gun.png')
gunX = random.randint(0, 736)
gunY = 50
gunX_change = 0.4
gunY_change = 0.4

# Bullet
bulletImg = pygame.image.load('bullets.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = -0.4
bullet_state = "ready"

# backgrounf
backgorund = pygame.image.load('background.png')


def Player(x, y):
    # Draw
    screen.blit(playerImg, (x, y))


def Gun(x, y):
    screen.blit(gunImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))


# Game loop for the main window
running = True
while running:

    screen.fill((90, 112, 22))
    screen.blit(backgorund, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If key keystroke is pressed check whether its right or left

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1
            if event.key == pygame.K_SPACE :
                if bullet_state == "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change

    gunY_change = 0

    if gunX >= 736:
        gunX_change = -0.4
        gunY_change = 10
    if gunX <= 0:
        gunX_change = 0.4
        gunY_change = 10
    if playerY >= 536 or playerY <= 150: playerY_change = 0
    if playerX >= 736 or playerX <= 0: playerX_change = 0

    gunX += gunX_change
    gunY += gunY_change

    bulletY += bulletY_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        if bulletY < -10: bullet_state = "ready"

    Player(playerX, playerY)
    Gun(gunX, gunY)

    pygame.display.update()
