import pygame

# General setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


# GLOBAL VARIABLES
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720 # 960
BG_COLOR = pygame.Color('#2F373F')
ACCENT_COLOR = (27, 35, 43)
MAIN_SCREEN_FONT = pygame.font.Font('freesansbold.ttf', 82)
BASIC_FONT = pygame.font.Font('freesansbold.ttf', 32)
COLLISION_SOUND = pygame.mixer.Sound("assets/pong.ogg")
SCORE_SOUND = pygame.mixer.Sound("assets/score.ogg")
MID_LINE = pygame.Rect(SCREEN_WIDTH / 2 - 2, 0, 4, SCREEN_HEIGHT)
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
