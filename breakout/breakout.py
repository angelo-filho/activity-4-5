import pygame

width, height = 600, 490
screen = pygame.display.set_mode((width, height))
background_colour = (0, 0, 0)
screen.fill(background_colour)
pygame.display.flip()

run = True


def move_bar():
    return null


def move_ball():
    return null


def collision_ball_wall():
    return null


def collision_ball_bricks():
    return null


def draw_bricks():
    return null


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
