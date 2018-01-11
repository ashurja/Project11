# Jamshed Ashurov
# 01/11/2018
# brick.py
# This file creates the bricks(images).

import pygame


# This class creates the Brick class of the game. It upload the image of the brick
class Brick(pygame.sprite.Sprite):

    def __init__(self, file_name):
        super().__init__()
        self.image = pygame.image.load(str(file_name))
        self.rect = self.image.get_rect()



