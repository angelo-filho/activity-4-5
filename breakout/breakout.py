from Classes.Paddle import Paddle
from Classes.Ball import Ball
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 680
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
background_colour = (0, 0, 0)
screen.fill(background_colour)
pygame.display.set_caption('BREAKOUT')
run = True
clock = pygame.time.Clock()
FPS = 60
color = 61, 164, 163
sprites = pygame.sprite.Group()

# Paddle
paddle = Paddle(color, 100, 20)
paddle.rect.x = 350
paddle.rect.y = 640

# Ball
ball = Ball(color, 20, 20)
ball.rect.x = 300
ball.rect.y = 350

sprites.add(paddle)
sprites.add(ball)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left()
    if keys[pygame.K_RIGHT]:
        paddle.move_right()

    sprites.update()

    if ball.rect.bottom >= HEIGHT + 30:
        ball.reset_ball()

    if pygame.sprite.collide_mask(ball, paddle) and ball.dy > 0:
        ball.collision_with_paddle(paddle.rect)

    screen.fill((0, 0, 0))
    sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
