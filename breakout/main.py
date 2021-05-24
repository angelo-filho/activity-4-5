import sys
import os

from random import randint
from model.Paddle import Paddle, PaddleRemake
from model.Ball import Ball
from model.Brick import Brick
from breakout.model.Item import *
from breakout.control.constants import *
import pygame
from pygame.locals import *

# Screen Init
pygame.init()
main_clock = pygame.time.Clock()
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
background_color = (0, 0, 0)
screen.fill(background_color)
pygame.display.set_caption('BREAKOUT')
icon = pygame.image.load('assets/atari.png')
pygame.display.set_icon(icon)
image = pygame.image.load('assets/screen_main.png')

# Screen init text
font = pygame.font.Font('assets/VT323-Regular.ttf', 45)
font_controls = pygame.font.Font('assets/VT323-Regular.ttf', 35)

# Pause text
pause_text = pygame.font.Font('assets/VT323-Regular.ttf', 32) \
    .render('Pause', True, pygame.color.Color('White'))
back_game = pygame.font.Font('assets/VT323-Regular.ttf', 32) \
    .render('Press s to back', True, pygame.color.Color('White'))

# Score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 40)
score_text = score_font.render('000   000', True, COLOR_BALL, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (200, 30)

background_music.play(-1)


# Function make bricks
def make_all_bricks(group_a, group_b):
    for i in range(6):
        for j in range(BRICKS_TOTAL_COLS):
            brick = None
            if i in [0, 1]:
                brick = Brick(COLOR_RED, BRICK_WIDTH, BRICK_HEIGHT, 5)
            elif i in [2, 3]:
                brick = Brick(COLOR_ORANGE, BRICK_WIDTH, BRICK_HEIGHT, 3)
            elif i in [4, 5]:
                brick = Brick(COLOR_GREEN, BRICK_WIDTH, BRICK_HEIGHT, 1)
            brick.rect.x = BRICKS_GAP * j + j * BRICK_WIDTH
            brick.rect.y = BRICKS_FIRST_ROW_Y + i * (BRICK_HEIGHT + BRICKS_GAP)
            group_a.add(brick)
            group_b.add(brick)


# Function random item
def make_random_item(brick):
    random_number = randint(0, 600)

    item = None

    if random_number < 20:
        item = LifeItem(COLOR_BALL, 32, 32)
    elif random_number < 40:
        item = GrowPaddleItem(COLOR_BALL, 32, 32)
    elif random_number < 60:
        item = GunItem(COLOR_BALL, 32, 32)

    if item:
        item.rect.center = brick.rect.center

        return item

    return None


# Function screen  init
def screen_init():
    click = False

    click_start_frames = 0

    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_start = font.render('Click to start', True, COLOR_BALL)
        font_start_rect = font_start.get_rect()
        font_start_rect.center = (300, 600)
        pos_x, pos_y = pygame.mouse.get_pos()
        if font_start_rect.collidepoint((pos_x, pos_y)):
            if click:
                menu()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        click_start_frames += 1

        if click_start_frames < 30:
            screen.blit(font_start, font_start_rect)

        if click_start_frames == 60:
            click_start_frames = 0

        pygame.display.update()
        main_clock.tick(FPS)


# Function menu
def menu():
    click = False
    image = pygame.image.load('assets/main_menu.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_games = font.render('Games', True, COLOR_BALL)
        font_controls = font.render('Controls', True, COLOR_BALL)
        font_credits = font.render('Credits', True, COLOR_BALL)
        font_exit = font.render('Exit', True, COLOR_BALL)
        font_games_rect = font_games.get_rect()
        font_controls_rect = font_controls.get_rect()
        font_credits_rect = font_credits.get_rect()
        font_exit_rect = font_exit.get_rect()
        font_games_rect.center = (300, 350)
        font_controls_rect.center = (300, 400)
        font_credits_rect.center = (300, 450)
        font_exit_rect.center = (300, 500)

        pos_x, pos_y = pygame.mouse.get_pos()

        if font_games_rect.collidepoint((pos_x, pos_y)):
            if click:
                games()

        if font_credits_rect.collidepoint((pos_x, pos_y)):
            if click:
                credits()

        if font_controls_rect.collidepoint((pos_x, pos_y)):
            if click:
                controls()

        if font_exit_rect.collidepoint((pos_x, pos_y)):
            if click:
                pygame.quit()
                sys.exit()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_games, font_games_rect)
        screen.blit(font_controls, font_controls_rect)
        screen.blit(font_credits, font_credits_rect)
        screen.blit(font_exit, font_exit_rect)
        pygame.display.update()
        main_clock.tick(FPS)


# Function controls
def controls():
    click = False
    image = pygame.image.load('assets/screen_controls.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_back = font_controls.render('back to menu', True, COLOR_BALL)
        font_back_rect = font_back.get_rect()
        font_back_rect.center = (300, 680)
        pos_x, pos_y = pygame.mouse.get_pos()

        if font_back_rect.collidepoint((pos_x, pos_y)):
            if click:
                back()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_back, font_back_rect)
        pygame.display.update()
        main_clock.tick(FPS)


# Function Games
def games():
    click = False
    image = pygame.image.load('assets/screen_games.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_classic_games = font.render('Classic', True, COLOR_BALL)
        font_remake_game = font.render('Remake', True, COLOR_BALL)
        font_back = font.render('back to menu', True, COLOR_BALL)
        font_classic_games_rect = font_classic_games.get_rect()
        font_remake_game_rect = font_remake_game.get_rect()
        font_back_rect = font_back.get_rect()
        font_classic_games_rect.center = (300, 350)
        font_remake_game_rect.center = (300, 400)
        font_back_rect.center = (300, 450)

        pos_x, pos_y = pygame.mouse.get_pos()

        if font_classic_games_rect.collidepoint((pos_x, pos_y)):
            if click:
                classic_game()

        if font_remake_game_rect.collidepoint((pos_x, pos_y)):
            if click:
                remake_game()

        if font_back_rect.collidepoint((pos_x, pos_y)):
            if click:
                back()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_classic_games, font_classic_games_rect)
        screen.blit(font_remake_game, font_remake_game_rect)
        screen.blit(font_back, font_back_rect)
        pygame.display.update()
        main_clock.tick(FPS)


# Function try again
def try_again(number):
    if number == 1:
        classic_game()
    else:
        remake_game()


# Function back
def back():
    menu()


# Function Credits
def credits():
    click = False
    image = pygame.image.load('assets/screen_credits.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_back = font.render('back to menu', True, COLOR_BALL)
        font_back_rect = font_back.get_rect()
        font_back_rect.center = (300, 670)

        pos_x, pos_y = pygame.mouse.get_pos()

        if font_back_rect.collidepoint((pos_x, pos_y)):
            if click:
                back()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_back, font_back_rect)
        pygame.display.update()
        main_clock.tick(FPS)


# Function Victory
def victory():
    click = False
    image = pygame.image.load('assets/screen_winner.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_winner = font.render('back to menu', True, COLOR_BALL)
        font_winner_rect = font_winner.get_rect()
        font_winner_rect.center = (300, 670)

        pos_x, pos_y = pygame.mouse.get_pos()

        if font_winner_rect.collidepoint((pos_x, pos_y)):
            if click:
                back()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_winner, font_winner_rect)
        pygame.display.update()
        main_clock.tick(FPS)


def loser(number):
    click = False
    image = pygame.image.load('assets/screen_loser.png')
    while True:
        screen.fill(COLOR_BLACK)
        screen.blit(image, (0, 0))
        font_loser = font.render('Try Again', True, COLOR_BALL)
        font_back = font.render('back to menu', True, COLOR_BALL)
        font_loser_rect = font_loser.get_rect()
        font_loser_rect.center = (300, 400)
        font_back_rect = font_back.get_rect()
        font_back_rect.center = (300, 470)
        pos_x, pos_y = pygame.mouse.get_pos()

        if font_loser_rect.collidepoint((pos_x, pos_y)):
            if click:
                try_again(number)

        if font_back_rect.collidepoint((pos_x, pos_y)):
            if click:
                back()

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        screen.blit(font_loser, font_loser_rect)
        screen.blit(font_back, font_back_rect)
        pygame.display.update()
        main_clock.tick(FPS)


# Classic Game
def classic_game():
    run = True
    sprites = pygame.sprite.Group()
    lives = LIVES
    score = SCORE
    level = ROUND

    # Paddle
    paddle = Paddle(350, HEIGHT - 40, 80, 20)

    # Ball
    ball = Ball(COLOR_BALL, 13, 13)
    ball.rect.x = -30
    ball.rect.y = -30

    sprites.add(ball)

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

        if ball.rect.bottom >= HEIGHT + 30 and ball.state == ball.MOVE_STATE:
            lives += 1
            ball.state = ball.RESTART_STATE
            paddle.recovery_weight()

        bricks_collided = pygame.sprite.spritecollide(ball, bricks, False)
        for brick in bricks_collided:
            if ball.can_collide:
                ball.collision_with_brick()
                score += brick.score
                brick.kill()

        if ball.rect.colliderect(paddle) and ball.dy > 0:
            ball.collision_with_paddle(paddle.rect)

            if ball.touch_amount == 15:
                paddle.lose_weight()

            if len(bricks) == 0:
                make_all_bricks(bricks, sprites)

        if len(bricks) == 0:
            level += 1

        if round == 1:
            victory()

        if lives == 4:
            loser(1)

        # Update score hud
        hud_score = score_font.render("{:03d}".format(int(str(lives)))
                                      + '        '
                                      + "{:03d}".format(int(str(score))),
                                      True, COLOR_BALL, COLOR_BLACK)
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        paddle.render(screen)
        screen.blit(hud_score, score_text_rect)
        pygame.display.flip()
        pygame.display.update()
        main_clock.tick(FPS)
    pygame.quit()
    sys.exit()


# Remake game
def remake_game():
    run = True
    sprites = pygame.sprite.Group()

    score = SCORE
    level = ROUND
    state = RUNNING

    # Paddle
    paddle = PaddleRemake(350, HEIGHT - 40, 80, 20)

    # Ball
    ball = Ball(COLOR_BALL, 13, 13)
    ball.rect.x = -30
    ball.rect.y = -30

    sprites.add(ball)

    # Bricks
    bricks = pygame.sprite.Group()
    make_all_bricks(bricks, sprites)

    # Items
    items = pygame.sprite.Group()

    # Bullets
    bullets = pygame.sprite.Group()

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    state = PAUSE
                if event.key == pygame.K_s:
                    state = RUNNING
        else:
            screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()

        if state == RUNNING:
            if keys[pygame.K_LEFT]:
                paddle.move_left()
            if keys[pygame.K_RIGHT]:
                paddle.move_right()
            sprites.update()
            bullets.update()
            paddle.update(bullets)
            # Ball collisions
            if ball.rect.bottom >= HEIGHT + 30 and ball.state == ball.MOVE_STATE:
                paddle.life -= 1
                ball.state = ball.RESTART_STATE
                paddle.recovery_weight()

        bricks_collided = pygame.sprite.spritecollide(ball, bricks, False)
        for brick in bricks_collided:
            if ball.can_collide:
                ball.collision_with_brick()

                item = make_random_item(brick)

                if item:
                    sprites.add(item)
                    items.add(item)

                score += brick.score
                brick.kill()

        if ball.rect.colliderect(paddle) and ball.dy > 0:
            ball.collision_with_paddle(paddle.rect)

            if ball.touch_amount == 26:
                paddle.lose_weight()

            if len(bricks) == 0:
                make_all_bricks(bricks, sprites)

        if len(bricks) == 0:
            level += 1

        if level == 1:
            victory()

        if paddle.life == 0:
            loser(2)

        # Player collision with items
        for item in items:
            if paddle.rect.colliderect(item.rect):
                paddle.collision_with_items(item)
                item.kill()

        # Bullets collisions
        for bullet in bullets:
            bricks_collided = pygame.sprite.spritecollide(bullet, bricks, False)
            for brick in bricks_collided:
                sound_hit_brick.play()
                item = make_random_item(brick)

                if item:
                    sprites.add(item)
                    items.add(item)

                bullet.kill()

                score += brick.score
                brick.kill()
        # Update score hud
        hud_score = score_font.render("{:03d}".format(int(str(paddle.life)))
                                      + '        '
                                      + "{:03d}".format(int(str(score))),
                                      True, COLOR_BALL, COLOR_BLACK)
        screen.fill((0, 0, 0))
        sprites.draw(screen)
        bullets.draw(screen)
        paddle.render(screen)
        screen.blit(hud_score, score_text_rect)
        if state == PAUSE:
            screen.blit(pause_text, (250, 350))
            screen.blit(back_game, (250, 400))
        pygame.display.flip()
        pygame.display.update()
        main_clock.tick(FPS)
    pygame.quit()
    sys.exit()


# Init
screen_init()
