import pygame

BLACK(0, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def collision_ball_wall(self):
        global ball_dx

        if ball.left <= 0 or ball.right >= size[0]:
            ball_dx *= -1
