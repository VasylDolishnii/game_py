import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

screen = width, heigth = 800 ,600

BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 0, 87, 184
YELLOW = 254, 221, 0

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = 1

is_working = True

while is_working: 
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    pressed_keys = pygame.key.get_pressed()

    main_surface.fill(BLACK)

    main_surface.blit(ball, ball_rect)

    if pressed_keys[K_DOWN] and not ball_rect.bottom >= heigth:
        ball_rect = ball_rect.move(0, ball_speed)

    if pressed_keys[K_UP] and not ball_rect.top < 0:
        ball_rect = ball_rect.move(0, -ball_speed)

    if pressed_keys[K_RIGHT] and not ball_rect.right >= width:
        ball_rect = ball_rect.move(ball_speed, 0)

    if pressed_keys[K_LEFT] and not ball_rect.left < 0:
        ball_rect = ball_rect.move(-ball_speed, 0)

    pygame.display.flip()