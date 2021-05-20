import pygame
from random import randint
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

        self.speed = 5
        self.dx = 1
        self.dy = 1

    def update(self):
        self.movement()

    def movement(self):
        self.rect.x += self.speed * self.dx
        self.rect.y += self.speed * self.dy

        self.collision_with_wall()

    def collision_with_wall(self):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.dx *= -1
        elif self.rect.top <= 0 and self.dy < 0:
            self.dy *= -1

    def randomize_angle(self, a, b, x_direction):
        random_angle = randint(a, b)
        angle = radians(random_angle)
        self.dx = cos(angle) * x_direction
        self.dy = -sin(angle)

    def collision_with_paddle(self, player_rect: pygame.rect.Rect):
        if player_rect.left <= self.rect.right < player_rect.left + 10:
            self.randomize_angle(20, 30, -1)
        elif player_rect.right >= self.rect.left > player_rect.right - 10:
            self.randomize_angle(20, 30, 1)
        elif player_rect.left + 10 <= self.rect.centerx < player_rect.centerx:
            self.randomize_angle(35, 45, -1)
        elif player_rect.right - 10 >= self.rect.centerx >= player_rect.centerx:
            self.randomize_angle(35, 45, 1)
