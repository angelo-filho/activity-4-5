import keyword
from _hashlib import HASH
import pygame

pygame.init()

WIDTH, HEIGHT = 893, 680
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
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


sprites.add(paddle)


def move_ball():
    ball.x += ball_dx
    ball.y += ball_dy

    collision_ball_wall()


def collision_ball_wall():
    global ball_dx

    if ball.left <= 0 or ball.right >= size[0]:
        ball_dx *= -1


def collision_ball_bricks():
    pass


def draw_bricks():
    pass


ball = pygame.rect.Rect(size[0] / 2, size[0] / 2, 20, 20)
ball_dx = 1
ball_dy = 1


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move_ball()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        paddle.moveRight(5)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (61, 164, 163), bar)

    pygame.display.flip()
    pygame.display.update()
pygame.quit()
