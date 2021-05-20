import sys

from model.Paddle import Paddle
from model.Ball import Ball
from model.Brick import Brick
from control.constants import *
import pygame
from pygame.locals import *

pygame.init()
main_clock = pygame.time.Clock()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
background_colour = (0, 0, 0)
screen.fill(background_colour)
pygame.display.set_caption('BREAKOUT')
icon = pygame.image.load('assets/atari.png')
pygame.display.set_icon(icon)


def menu():
    click = False
    while True:
        pos_x, pos_y = pygame.mouse.get_pos()
        button_game = pygame.Rect(50, 100, 255, 255)

        if button_game.collidepoint((pos_x, pos_y)):
            if click:
                game()

        pygame.draw.rect(screen, (255, 0, 0), button_game)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        main_clock.tick(60)


def game():
    run = True
    sprites = pygame.sprite.Group()

    # Paddle
    paddle = Paddle(COLOR_PADDLE, 100, 30)
    paddle.rect.x = 350
    paddle.rect.y = 640

    # Ball
    ball = Ball(COLOR_BALL, 20, 20)
    ball.rect.x = 300
    ball.rect.y = 350

    # Ball
    ball = Ball(COLOR_BALL, 15, 15)
    ball.rect.x = 300
    ball.rect.y = 350

    # Bricks
    for i in range(7):
        brick = Brick(COLOR_RED, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 60
        sprites.add(brick)
    for i in range(7):
        brick = Brick(COLOR_ORANGE, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 5 + i * 100
        brick.rect.y = 100
        sprites.add(brick)
    for i in range(7):
        brick = Brick(COLOR_GREEN, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 60 + i * 100
        brick.rect.y = 140
        sprites.add(brick)

    sprites.add(paddle)
    sprites.add(ball)

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        sprites.update()

        if ball.rect.bottom >= HEIGHT + 30:
            ball.state = ball.RESTART_STATE

        if pygame.sprite.collide_mask(ball, paddle) and ball.dy > 0:
            ball.collision_with_paddle(paddle.rect)

        screen.fill((0, 0, 0))
        sprites.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        main_clock.tick(FPS)
    pygame.quit()
    sys.exit()


menu()
