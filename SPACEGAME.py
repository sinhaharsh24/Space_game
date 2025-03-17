import pygame
import random
import math

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Game")
icon = pygame.image.load('img/spaceship.png')
pygame.display.set_icon(icon)

# Background
background = pygame.image.load('img/spacegamebg.png')
bg = pygame.transform.scale(background, (800, 600))
q = 0
height = 600

# Player
playerimg = pygame.image.load('img/spaceshipplayer.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy setup
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('img/spaceshipenemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bullet = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"  # ready - bullet is off screen

# Score
score = 0
font = pygame.font.Font('font/Coffee Spark.ttf', 32)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('font/Coffee Spark.ttf', 64)

# Function to show score
def show_score(x, y):
    score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))

# Collision detection
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < 27

# Game over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 250))

# Draw player
def player(x, y):
    screen.blit(playerimg, (x, y))

# Draw enemy
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

# Fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 18, y + 20))

# Main game loop
run = True
while run:

    screen.fill((0, 0, 0))

    # Background scrolling
    screen.blit(background, (0, q))
    screen.blit(background, (0, height + q))
    if q == -height:
        q = 0
    q -= 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Keydown events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)

        # Keyup events
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 720:
        playerX = 720

    # Enemy movement
    for i in range(num_of_enemies):

        # Game over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 1000
            game_over_text()
            show_score(textX, textY)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 6
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 720:
            enemyX_change[i] = -6
            enemyY[i] += enemyY_change[i]

        # Collision detection
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw player and score
    player(playerX, playerY)
    show_score(textX, textY)

    # Update display
    pygame.display.update()

pygame.quit()
