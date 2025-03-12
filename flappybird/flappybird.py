import pygame
import neat
import time
import os
WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","bird3.png")))]
PIPE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","pipe.png")))]
BASE_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","base.png")))]
BG_IMG = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs_b286d95d6d","bg.png")))]
