import pygame
from pygame import *
import sys
from random import randint
from math import radians, cos, sin

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY_DARK = (134, 134, 134)
COLOR_GRAY_DARKER = (104, 104, 104)

SCORE_MAX = 2

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font.render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1_image = pygame.image.load("assets/player.png").convert()
player_1 = player_1_image.get_rect().move(50, 300)
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2_image = pygame.image.load("assets/player.png").convert()
player_2 = player_2_image.get_rect().move(1180, 300)
player_2_speed = 3


# ball
ball_image = pygame.image.load("assets/ball.png").convert()
ball = ball_image.get_rect().move(640, 360)
ball_dx = 1
ball_dy = 1
ball_speed = 5
MIN_BALL_SPEED = 5
MAX_BALL_SPEED = 9


def randomize_angle():
    global ball_dx, ball_dy

    random_angle = randint(20, 45)
    angle = radians(random_angle)
    ball_dx = cos(angle)
    ball_dy = sin(angle)


def change_angle(player_rect: pygame.rect.Rect, x_direction):
    global ball_dx, ball_dy

    if player_rect.top <= ball.bottom <= player_rect.top + 60:
        ball_dy *= -1
        ball_dx *= x_direction
    elif player_rect.bottom >= ball.top >= player_rect.bottom - 60:
        ball_dx *= x_direction
    elif player_rect.centery - 15 < ball.centery < player_rect.centery + 15:
        ball_dy = 0
        ball_dx *= x_direction * 1.5


# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()
game_state = "Menu"


# Menu loop
def main_menu():
    global game_state

    click = False
    while True:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        draw_text("Pong", victory_font, (255, 255, 255), screen, screen.get_rect().centery + 80, 170)

        button_1 = pygame.Rect(screen.get_rect().centery + 170, 370, 200, 60)
        button_2 = pygame.Rect(screen.get_rect().centery + 170, 470, 200, 60)

        color1 = COLOR_GRAY_DARK
        color2 = COLOR_GRAY_DARK

        if button_1.collidepoint((mx, my)):
            color1 = COLOR_GRAY_DARKER
            if click:
                game_state = "Game"
                break
        if button_2.collidepoint((mx, my)):
            color2 = COLOR_GRAY_DARKER
            if click:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(screen, color1, button_1)
        pygame.draw.rect(screen, color2, button_2)
        draw_text("Play", score_font, (255, 255, 255), screen, screen.get_rect().centery + 185, button_1.y + 10)
        draw_text("Exit", score_font, (255, 255, 255), screen, screen.get_rect().centery + 185, button_2.y + 10)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        game_clock.tick(60)


while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    if game_state == "Menu":
        main_menu()

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX and game_state == "Game":
        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball.bottom > 720:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball.top <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        if ball.colliderect(player_1) and ball_dx < 0:
            ball_speed = min(ball_speed + 0.2, MAX_BALL_SPEED)
            randomize_angle()
            change_angle(player_1, 1)
            bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        elif ball.colliderect(player_2) and ball_dx > 0:
            ball_speed = min(ball_speed + 0.2, MAX_BALL_SPEED)
            randomize_angle()
            change_angle(player_2, -1)
            bounce_sound_effect.play()

        # scoring points
        if ball.x < -50:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            ball_speed = MIN_BALL_SPEED
            scoring_sound_effect.play()
        elif ball.x > 1320:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            ball_speed = MIN_BALL_SPEED
            scoring_sound_effect.play()

        # ball movement
        ball.x += ball_speed * ball_dx
        ball.y += ball_speed * ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1.y -= 5
        else:
            player_1.y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1.y += 5
        else:
            player_1.y += 0

        # player 1 collides with upper wall
        if player_1.y <= 0:
            player_1.y = 0

        # player 1 collides with lower wall
        elif player_1.y >= 570:
            player_1.y = 570

        # player 2 "Artificial Intelligence"
        if player_2.centery < ball.y:
            player_2.y += player_2_speed
        elif player_2.centery > ball.y:
            player_2.y -= player_2_speed

        # player 2 "Artificial Intelligence" collides with up and down wall
        if player_2.y <= 0:
            player_2.y = 0
        elif player_2.y >= 570:
            player_2.y = 570

        # update score hud
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball_image, (ball.x, ball.y))
        screen.blit(player_1_image, (50, player_1.y))
        screen.blit(player_2_image, (1180, player_2.y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
