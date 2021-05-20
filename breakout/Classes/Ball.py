import pygame

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

    def collision_ball_wall(self):
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.dx *= -1
