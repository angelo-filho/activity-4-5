import pygame
from breakout.model.Bullet import Bullet
from breakout.control.constants import COLOR_BLACK, COLOR_BALL


class Gun(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)
        self.rect = self.image.get_rect()
        pygame.draw.polygon(self.image, color, [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright])

        self.fire_rate = 0
        self.MAX_FIRE_RATE = 80

    def fire(self, bullets):
        self.fire_rate += 1

        if self.fire_rate > self.MAX_FIRE_RATE:
            bullet = Bullet(COLOR_BALL, 7, 7)
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.top
            bullets.add(bullet)

            self.fire_rate = 0
