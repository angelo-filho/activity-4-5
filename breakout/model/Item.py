import os

import pygame
from breakout.control.constants import COLOR_BLACK
from breakout.control.constants import HEIGHT


class Item(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.GRAVITY = 3

    def update(self):
        self.rect.y += self.GRAVITY

        if self.rect.y >= HEIGHT:
            self.kill()


class GrowPaddleItem(Item):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "grow_item.png")))


class LifeItem(Item):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "life_item.png")))


class GunItem(Item):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
        self.image = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "gun_item.png")))
