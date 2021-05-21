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

# Score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
score_text = score_font.render('000      000', True, COLOR_BALL, background_color)
score_text_rect = score_text.get_rect()
score_text_rect.center = (370, 30)

def make_all_bricks(group_a, group_b):
    for i in range(11):
        brick = Brick(COLOR_RED, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 20 + i * 70
        brick.rect.y = 60
        group_a.add(brick)
        group_b.add(brick)
    for i in range(11):
        brick = Brick(COLOR_ORANGE, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 20 + i * 70
        brick.rect.y = 100
        group_a.add(brick)
        group_b.add(brick)
    for i in range(11):
        brick = Brick(COLOR_GREEN, BRICK_WIDTH, BRICK_HEIGHT)
        brick.rect.x = 20 + i * 70
        brick.rect.y = 140
        group_a.add(brick)
        group_b.add(brick)


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
    paddle = Paddle(COLOR_PADDLE, 100, 20)
    paddle.rect.x = 350
    paddle.rect.y = 640

    # Ball
    ball = Ball(COLOR_BALL, 15, 15)
    ball.rect.x = 300
    ball.rect.y = 350

    sprites.add(ball)
    sprites.add(paddle)

    # Bricks
    bricks = pygame.sprite.Group()
    make_all_bricks(bricks, sprites)

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

        bricks_collided = pygame.sprite.spritecollide(ball, bricks, False)
        for brick in bricks_collided:
            if ball.can_collide:
                ball.collision_with_brick()
                brick.kill()

        if pygame.sprite.collide_mask(ball, paddle) and ball.dy > 0:
            ball.collision_with_paddle(paddle.rect)

        # Update score hud
        hud_score = score_font.render("{:03d}".format(int(str(lives)))
                                      + '        '
                                      + "{:03d}".format(int(str(score))),
                                      True, COLOR_BALL, background_color)
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        screen.blit(hud_score, score_text_rect)
        pygame.display.flip()
        pygame.display.update()
        main_clock.tick(FPS)
    pygame.quit()
    sys.exit()


menu()
