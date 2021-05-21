import pygame
from random import randint, choice
from math import cos, sin, radians
from breakout.control.constants import WIDTH, COLOR_BLACK


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.MIN_SPEED = 7
        self.MAX_SPEED = 12
        self.speed_increment = 0.5
        self.speed = self.MIN_SPEED

        self.dx = 1
        self.dy = 1

        self.restart_frames = 0
        self.MAX_RESTART_FRAMES = 120

        self.MOVE_STATE = 0
        self.RESTART_STATE = 1
        self.state = self.MOVE_STATE

        self.can_collide = True
        self.frames_can_collide = 0
        self.MAX_FRAMES_CAN_COLLIDE = 16

    def update(self):
        if self.state == self.MOVE_STATE:
            self.move_state_update()
        elif self.state == self.RESTART_STATE:
            self.restart_state_update()

    def move_state_update(self):
        self.movement()
        self.collision_with_wall()

        if not self.can_collide:
            self.frames_can_collide += 1
            if self.frames_can_collide == self.MAX_FRAMES_CAN_COLLIDE:
                self.frames_can_collide = 0
                self.can_collide = True

    def movement(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

    def collision_with_wall(self):
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        elif self.rect.top <= 0 and self.dy < 0:
            self.dy *= -1

    def collision_with_paddle(self, player_rect: pygame.rect.Rect):
        self.speed = min(self.speed + self.speed_increment, self.MAX_SPEED)

        if self.rect.centerx < player_rect.centerx:
            self.randomize_angle(35, 60, -1)
        elif self.rect.centerx >= player_rect.centerx:
            self.randomize_angle(35, 60, 1)

    def collision_with_brick(self):
        self.speed = min(self.speed + self.speed_increment, self.MAX_SPEED)
        self.dy *= -1
        self.can_collide = False

    def randomize_angle(self, a, b, x_direction, y_direction=-1):
        random_angle = randint(a, b)
        angle = radians(random_angle)
        self.dx = cos(angle) * x_direction
        self.dy = sin(angle) * y_direction

    def restart_state_update(self):
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
