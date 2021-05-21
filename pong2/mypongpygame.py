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
score_text = score_font.render('0 x 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (650, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (420, 350)


def draw_text(text, font, color, surface, x, y):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')


class Entity:
    def __init__(self, image, x_start, y_start):
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect().move(x_start, y_start)
        self.x_start = x_start
        self.y_start = y_start

    def restart_position(self):
        self.rect.x, self.rect.y = self.x_start, self.y_start

    def render(self):
        screen.blit(self.image, [self.rect.x, self.rect.y])


class Player1(Entity):
    def __init__(self, image, x_start, y_start):
        super().__init__(image, x_start, y_start)
        self.speed = 5
        self.move_up = False
        self.move_down = False

    def update(self):
        self.movement()
        self.collide_with_walls()

    def movement(self):
        # player 1 up movement
        if self.move_up:
            self.rect.y -= self.speed
        else:
            self.rect.y += 0

        # player 1 down movement
        if self.move_down:
            self.rect.y += self.speed
        else:
            self.rect.y += 0

    def collide_with_walls(self):
        # player 1 collides with upper wall
        if self.rect.y <= 0:
            self.rect.y = 0

        # player 1 collides with lower wall
        elif self.rect.y >= 570:
            self.rect.y = 570


# player 1
player1 = Player1("assets/player.png", 50, 300)


class Player2(Entity):
    def __init__(self, image, x_start, y_start):
        super().__init__(image, x_start, y_start)
        self.speed = 3

    def update(self):
        self.movement()
        self.collides_with_walls()

    def movement(self):
        # player 2 "Artificial Intelligence"
        if self.rect.centery < ball.rect.y:
            self.rect.y += self.speed
        elif self.rect.centery > ball.rect.y:
            self.rect.y -= self.speed

    def collides_with_walls(self):
        # player 2 "Artificial Intelligence" collides with up and down wall
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 570:
            self.rect.y = 570


# player 2 - robot
player2 = Player2("assets/player.png", 1180, 300)


class Ball(Entity):
    def __init__(self, image, x_start, y_start):
        super(Ball, self).__init__(image, x_start, y_start)
        self.dx = 1
        self.dy = 1
        self.speed = 5
        self.MIN_SPEED = 5
        self.MAX_SPEED = 9

    def update(self):
        self.movement()
        self.collision_with_wall()

        # ball collision with the player 1 's paddle
        if self.rect.colliderect(player1.rect) and ball.dx < 0:
            self.collision_with_paddles()
            self.change_angle(player1.rect, 1)
        # ball collision with the player 2 's paddle
        elif ball.rect.colliderect(player2) and self.dx > 0:
            self.collision_with_paddles()
            self.change_angle(player2.rect, -1)

    def movement(self):
        # ball movement
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

    def collision_with_paddles(self):
        self.speed = min(self.speed + 0.2, self.MAX_SPEED)
        self.randomize_angle()
        bounce_sound_effect.play()

    def collision_with_wall(self):
        # ball collision with the wall
        if self.rect.bottom > 720:
            ball.dy *= -1
            bounce_sound_effect.play()
        elif ball.rect.top <= 0:
            ball.dy *= -1
            bounce_sound_effect.play()

    def randomize_angle(self):
        random_angle = randint(20, 45)
        angle = radians(random_angle)
        self.dx = cos(angle)
        self.dy = sin(angle)

    def change_angle(self, player_rect: pygame.rect.Rect, x_direction):
        if player_rect.top <= self.rect.bottom <= player_rect.top + 60:
            self.dy *= -1
            self.dx *= x_direction
        elif player_rect.bottom >= self.rect.top >= player_rect.bottom - 60:
            self.dx *= x_direction
        elif player_rect.centery - 15 < self.rect.centery < player_rect.centery + 15:
            self.dy = 0
            self.dx *= x_direction * 1.5

    def restart_ball(self):
        self.restart_position()
        self.randomize_angle()
        self.dy = randint(-1, 1)
        self.speed = self.MIN_SPEED


# ball
ball = Ball("assets/ball.png", 640, 360)

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


def restart_game():
    global score_1, score_2
    score_1 = 0
    score_2 = 0
    player1.restart_position()
    player2.restart_position()
    ball.restart_ball()


press_r_frames = 0

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                player1.move_up = True
            if event.key == K_DOWN:
                player1.move_down = True
            if event.key == K_r and game_state == "Game" and (score_1 == SCORE_MAX or score_2 == SCORE_MAX):
                restart_game()

        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                player1.move_up = False
            if event.key == K_DOWN:
                player1.move_down = False

    if game_state == "Menu":
        main_menu()

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX and game_state == "Game":
        # clear screen
        screen.fill(COLOR_BLACK)

        # scoring points
        if ball.rect.x < -50:
            ball.restart_ball()
            score_2 += 1
            scoring_sound_effect.play()
        elif ball.rect.x > 1320:
            ball.restart_ball()
            score_1 += 1
            scoring_sound_effect.play()

        # update objects
        score_text = score_font.render(str(score_1) + ' x ' + str(score_2), True, COLOR_WHITE, COLOR_BLACK)
        player1.update()
        player2.update()
        ball.update()

        # drawing objects
        ball.render()
        player1.render()
        player2.render()
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        press_r_frames += 1
        if press_r_frames >= 30:
            draw_text('PRESS R TO RESTART', score_font, COLOR_WHITE, screen, 260, 600)
            if press_r_frames >= 60:
                press_r_frames = 0

        if score_1 == SCORE_MAX:
            draw_text("VICTORY", victory_font, COLOR_WHITE, screen, victory_text_rect.x, victory_text_rect.y)
        else:
            draw_text("DEFEAT", victory_font, COLOR_WHITE, screen, 360, victory_text_rect.y)
        screen.blit(score_text, score_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
