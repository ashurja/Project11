# Jamshed Ashurov
# 12/16/2017
# paddle.py
# This file creates paddle and function to move the ball

import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, mainsurface):
        super().__init__()
        self.mainsurface = mainsurface
        self.WIDTH = 60
        self.HEIGHT = 10
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(color)

    def move(self, xpos):
        """
        This function determines the x coordinate of the mouse and sets it to the middle of the paddle
        :param xpos:
        :return:
        """
        self.rect.centerx = xpos
