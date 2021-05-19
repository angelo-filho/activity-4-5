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
paddle = Paddle(color, 100, 30)
paddle.rect.x = 350
paddle.rect.y = 560

ball = Ball(size[0] / 2, size[0] / 2, 20)
ball.rect.x = 1
ball.rect.y = 1

sprites.add(paddle)


def collision_ball_bricks():
    pass


def draw_bricks():
    pass


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move_ball()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ball)
    sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
