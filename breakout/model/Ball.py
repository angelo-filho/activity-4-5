import pygame
from random import randint, choice
from math import cos, sin, radians

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.MIN_SPEED = 5
        self.MAX_SPEED = 10
        self.speed_increment = 0.5
        self.speed = self.MIN_SPEED

        self.dx = 1
        self.dy = 1

        self.restart_frames = 0
        self.MAX_RESTART_FRAMES = 120

        self.MOVE_STATE = 0
        self.RESTART_STATE = 1
        self.state = self.MOVE_STATE

    def update(self):
        if self.state == self.MOVE_STATE:
            self.movement()
        elif self.state == self.RESTART_STATE:
            self.restart_update()

    def movement(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

        self.collision_with_wall()

    def collision_with_wall(self):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.dx *= -1
        elif self.rect.top <= 0 and self.dy < 0:
            self.dy *= -1

    def collision_with_paddle(self, player_rect: pygame.rect.Rect):
        self.speed = min(self.speed + self.speed_increment, self.MAX_SPEED)

        if player_rect.left <= self.rect.right < player_rect.left + 10:
            self.randomize_angle(20, 30, -1)
        elif player_rect.right >= self.rect.left > player_rect.right - 10:
            self.randomize_angle(20, 30, 1)
        elif player_rect.left + 10 <= self.rect.centerx < player_rect.centerx:
            self.randomize_angle(35, 45, -1)
        elif player_rect.right - 10 >= self.rect.centerx >= player_rect.centerx:
            self.randomize_angle(35, 45, 1)

    def collision_with_brick(self, brick_rect):
        self.speed = min(self.speed + self.speed_increment, self.MAX_SPEED)

        if brick_rect.bottom - self.rect.top < 3:
            self.dy *= -1

    def randomize_angle(self, a, b, x_direction, y_direction=-1):
        random_angle = randint(a, b)
        angle = radians(random_angle)
        self.dx = cos(angle) * x_direction
        self.dy = sin(angle) * y_direction

    def restart_update(self):
        self.restart_frames += 1
        if self.restart_frames == self.MAX_RESTART_FRAMES:
            self.restart_frames = 0
            self.reset_ball()
            self.state = self.MOVE_STATE

    def reset_ball(self):
        self.rect.x = randint(200, 600)
        self.rect.y = 350
        self.randomize_angle(25, 45, choice([1, -1]), 1)
        self.speed = self.MIN_SPEED
