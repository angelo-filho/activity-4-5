import pygame
from breakout.control.constants import WIDTH, COLOR_PADDLE
from breakout.model.Item import *


class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

        self.speed = 12

        self.normal_width = width
        self.short_width = width - 30

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


class PaddleRemake(Paddle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

        self.huge_width = self.normal_width + 30

        self.NORMAL_STATE = 0
        self.HUGE_STATE = 1
        self.current_state = self.NORMAL_STATE

        self.frames_power_up = 0
        self.MAX_FRAMES_POWER_UP = 60 * 6

    def update(self):

        if self.current_state == self.NORMAL_STATE:
            self.normal_state_update()
        else:
            self.frames_power_up += 1

            if self.frames_power_up > self.MAX_FRAMES_POWER_UP:
                self.frames_power_up = 0
                self.current_state = self.NORMAL_STATE

            if self.current_state == self.HUGE_STATE:
                self.huge_state_update()

    def normal_state_update(self):
        self.rect.width = self.normal_width

    def huge_state_update(self):
        self.rect.width = self.huge_width

    def collision_with_items(self, item):
        self.frames_power_up = 0
        if type(item) == GrowPaddleItem:
            self.current_state = self.HUGE_STATE
