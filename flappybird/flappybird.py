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

class Bird:
    IMGS = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y
    
    def move(self):
        self.tick_count += 1

        d = self.vel * self.tick_count + 1.15 * self.tick_count ** 2
        if d >= 16:
            d = 16
        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.title = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tily -= self.ROT_VEL
while True:
