# Jamshed Ashurov
# 12/16/2017
# brick.py
# This file creates the bricks.

import pygame


class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color, mainsurface):
        super().__init__()
        self.mainsurface = mainsurface
        self.height = height
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image.fill(color)
