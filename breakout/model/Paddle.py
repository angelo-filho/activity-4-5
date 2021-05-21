import pygame
from breakout.control.constants import WIDTH, COLOR_PADDLE


class Paddle:
    def __init__(self,x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = 12

        self.normal_width = width
        self.short_width = width - 20

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right >= 600:
            self.rect.x = WIDTH - self.rect.width

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = 0

    def lose_weight(self):
        self.rect.width = self.short_width

    def recovery_weight(self):
        self.rect.width = self.normal_width

    def render(self, screen):
        pygame.draw.rect(screen, COLOR_PADDLE, self.rect)
