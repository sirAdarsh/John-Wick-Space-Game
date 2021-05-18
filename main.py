import pygame
import random
import math

from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("John Wick 4")

# Score
score_val = 0
font = pygame.font.Font('freesansbold.ttf', 32)

game_over_font = pygame.font.Font('freesansbold.ttf', 70)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("SCORE : " + str(score_val), True, (210, 100, 10))
    screen.blit(score, (x, y))

#Game Over
def game_over(x, y):
    game_over_text = game_over_font.render("GAME OVER", True, (250, 50, 0))
    screen.blit(game_over_text, (x,y))

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy

gunImg = []
gunX = []
gunY = []
gunX_change = []
gunY_change = []

num_of_enemies = 6

for i in range(num_of_enemies):
    gunImg.append(pygame.image.load('gun.png'))
    gunX.append(random.randint(0, 736))
    gunY.append(0)
    gunX_change.append(0.4)
    gunY_change.append(0.4)

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


def Gun(x, y, i):
    screen.blit(gunImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enX, enY, bulX, bulY):
    distance = math.sqrt(math.pow(enX - bulX, 2) + math.pow(enY - bulY, 2))
    if distance < 50:
        return True
    return False


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
            if event.key == pygame.K_SPACE:
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

    for i in range(num_of_enemies):

        #Game Over
        if gunY[i] > 250:
            for j in range (num_of_enemies):
                gunY[j]=1000
            game_over(100,300)
            break

        gunY_change[i] = 0
        if gunX[i] >= 736:
            gunX_change[i] = -0.4
            gunY_change[i] = 110
        if gunX[i] <= 0:
            gunX_change[i] = 0.4
            gunY_change[i] = 110
        gunX[i] += gunX_change[i]
        gunY[i] += gunY_change[i]

        collision = isCollision(bulletX, bulletY, gunX[i], gunY[i])
        if collision:
            score_val += 1
            bullet_state = "ready"
            gunX[i] = random.randint(0, 736)
            gunY[i] = 50

        Gun(gunX[i], gunY[i], i)

    if playerY >= 536 or playerY <= 150: playerY_change = 0
    if playerX >= 736 or playerX <= 0: playerX_change = 0

    bulletY += bulletY_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        if bulletY < -10: bullet_state = "ready"

    Player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
