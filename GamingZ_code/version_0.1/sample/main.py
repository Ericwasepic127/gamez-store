import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 600))
clock = pygame.time.Clock()

player_x = 200
blocks = [[random.randint(0, 350), random.randint(-100, 0)] for _ in range(5)]

running = True
while running:
    screen.fill((0, 0, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= 5
    if keys[pygame.K_RIGHT]: player_x += 5

    pygame.draw.rect(screen, (0, 255, 0), (player_x, 550, 50, 50))
    for b in blocks:
        b[1] += 3
        pygame.draw.rect(screen, (255, 0, 0), (b[0], b[1], 50, 50))
        if b[1] > 600: b[1] = random.randint(-100, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
