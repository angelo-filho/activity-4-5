import pygame

width, height = 893, 1000
size = (width, height)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
background_colour = (0, 0, 0)
screen.fill(background_colour)
pygame.display.set_caption('BREAKOUT')
run = True
clock = pygame.time.Clock()
FPS = 60


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
    pygame.display.update()
pygame.quit()
