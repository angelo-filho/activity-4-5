import pygame
import os

pygame.mixer.init()

FPS = 60
COLOR_BLACK = 0, 0, 0
RUNNING = 0
PAUSE = 1
LIVES = 0
ROUND = 0
SCORE = 0
COLOR_PADDLE = 61, 164, 163
COLOR_BALL = 255, 255, 255
# Color of Bricks
COLOR_GREEN = 0, 255, 0
COLOR_ORANGE = 255, 165, 0
COLOR_RED = (255, 0, 0)
WIDTH, HEIGHT = 600, 700

BRICKS_TOTAL_COLS = 11
BRICKS_FIRST_ROW_Y = 80
BRICKS_GAP = 5
BRICK_HEIGHT = 15
BRICK_WIDTH = 50

sound_hit_wall = pygame.mixer.Sound(os.path.join("assets", "sounds_wall.wav"))
sound_hit_brick = pygame.mixer.Sound(os.path.join("assets", "sounds_brick.wav"))
sound_hit_paddle = pygame.mixer.Sound(os.path.join("assets", "sounds_paddle.wav"))
background_music = pygame.mixer.Sound(os.path.join("assets", "background_music.wav"))
background_music.set_volume(0.03)
