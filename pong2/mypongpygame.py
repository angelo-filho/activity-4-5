import pygame
from random import randint
from math import radians, cos, sin

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

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
ball_speed = 7


def randomize_angle():
    global ball_dx, ball_dy

    random_angle = randint(45, 55)
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
        ball_dx *= x_direction * 2


# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

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

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:
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
            randomize_angle()
            change_angle(player_1, 1)
            bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if ball.colliderect(player_2) and ball_dx > 0:
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
            scoring_sound_effect.play()
        elif ball.x > 1320:
            ball.x = 640
            ball.y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
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
