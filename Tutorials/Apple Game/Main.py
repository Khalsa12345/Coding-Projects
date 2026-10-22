import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((350, 600))
clock = pygame.time.Clock()

class Apple:
    def __init__(self, image, position, speed):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

# Variables
speed = 3
score = 0
game_over_flag = False

# Constants
TILESIZE = 32

# Floor
floor_image = pygame.image.load('assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE * 15, TILESIZE * 5))
floor_rect = floor_image.get_rect(bottomleft=(0, screen.get_height()))

# Player
player_image = pygame.image.load('assets/player_static.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE * 2))
player_rect = player_image.get_rect(center=(screen.get_width() / 2,
                                            screen.get_height() - floor_image.get_height() - (player_image.get_height() / 2)))

# Apples
apple_image = pygame.image.load('assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))

apples = [
    Apple(apple_image, (100, 0), 3),
    Apple(apple_image, (300, 0), 3),
]

# Fonts
font = pygame.font.Font('assets/PixeloidMono.ttf', TILESIZE // 2)
game_over_font = pygame.font.Font('assets/PixeloidMono.ttf', TILESIZE)

# Sound effects
pickup = pygame.mixer.Sound('assets/powerup.mp3')
pickup.set_volume(0.1)

def reset_game():
    global speed, score, apples, game_over_flag
    speed = 3
    score = 0
    game_over_flag = False
    apples = [
        Apple(apple_image, (100, 0), 3),
        Apple(apple_image, (300, 0), 3),
    ]

def game_over():
    screen.fill('black')
    game_over_text = game_over_font.render('GAME OVER', True, 'red')
    score_text = font.render(f'Final Score: {score}', True, 'white')
    restart_text = font.render('Press R to Restart', True, 'white')

    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, 200))
    screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300))
    screen.blit(restart_text, (screen.get_width() // 2 - restart_text.get_width() // 2, 350))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                return

def update():
    global speed, score, game_over_flag

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:  # Move left
        player_rect.x -= 8
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:  # Move right
        player_rect.x += 8

    # Apple Management
    for apple in apples:
        apple.move()
        if apple.rect.colliderect(floor_rect):
            game_over_flag = True  # Trigger game over
        elif apple.rect.colliderect(player_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50, 300), -50), speed))
            speed += 0.1
            score += 1
            pickup.play()

def draw():
    screen.fill('lightblue')
    screen.blit(floor_image, floor_rect)
    screen.blit(player_image, player_rect)

    for apple in apples:
        screen.blit(apple.image, apple.rect)

    score_text = font.render(f'Score: {score}', True, "white")
    screen.blit(score_text, (5, 5))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_over_flag:
        game_over()
    
    update()
    draw()

    clock.tick(60)
    pygame.display.update()
