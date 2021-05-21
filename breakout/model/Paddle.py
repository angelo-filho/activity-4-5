import pygame
BLACK = (0, 0, 0)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.speed = 10

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right >= 600:
            self.rect.x = 800 - self.rect.width

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
