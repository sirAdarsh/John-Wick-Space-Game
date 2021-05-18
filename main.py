import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("John Wick 4")


# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


def Player(x, y):
    # Draw
    screen.blit(playerImg, (x,y))


# Game loop for the main window
running = True
while running:

    screen.fill((90, 112, 22))



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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    if playerY >= 536 or playerY <= 0: playerY_change = 0
    if playerX >= 736 or playerX <= 0: playerX_change = 0
    Player(playerX, playerY)
    pygame.display.update()