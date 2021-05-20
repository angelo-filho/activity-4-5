from model.Paddle import Paddle
from model.Ball import Ball
from brick_in_the_wall import Brick
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 680
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
background_colour = (0, 0, 0)
screen.fill(background_colour)
pygame.display.set_caption('BREAKOUT')
icon = pygame.image.load('assets/atari.png')
pygame.display.set_icon(icon)

run = True
clock = pygame.time.Clock()
FPS = 60
COLOR_PADDLE = 61, 164, 163
COLOR_BALL = 255, 255, 255

# Brick Colors
COLOR_GREEN = (0, 255, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_RED = (255, 0, 0)

# Brick size
BRICK_HEIGHT = 40
BRICK_WIDTH = 90

sprites = pygame.sprite.Group()

# Paddle
paddle = Paddle(COLOR_PADDLE, 100, 20)
paddle.rect.x = 350
paddle.rect.y = 640


# Ball
ball = Ball(COLOR_BALL, 15, 15)
ball.rect.x = 300
ball.rect.y = 350

sprites.add(paddle)
sprites.add(ball)

# Create Bricks
all_bricks = pygame.sprite.Group()
for i in range(7):
    brick = Brick(COLOR_RED, BRICK_WIDTH, BRICK_HEIGHT)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(COLOR_ORANGE, BRICK_WIDTH, BRICK_HEIGHT)
    brick.rect.x = 5 + i * 100
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks.add(brick)
for i in range(7):
    brick = Brick(COLOR_GREEN, BRICK_WIDTH, BRICK_HEIGHT)
    brick.rect.x = 60 + i * 100
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks.add(brick)

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
    all_sprites_list.draw(screen)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
