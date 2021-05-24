from breakout.control.constants import COLOR_BLACK


class Bullet(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(COLOR_BLACK)
        self.image.set_colorkey(COLOR_BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

        self.speed = 4

    def update(self):
        self.rect.y -= self.speed
