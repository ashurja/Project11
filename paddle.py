# Jamshed Ashurov
# 01/11/2018
# paddle.py
# This file creates paddle and function to move the ball

import pygame


# Creates the Paddle class of the game. It loads the image of the paddle and moves it.
class Paddle(pygame.sprite.Sprite):

    def __init__(self, mainsurface):
        super().__init__()
        self.mainsurface = mainsurface
        self.image = pygame.image.load("water-1018808_960_720.jpg")
        self.rect = self.image.get_rect()

    def move(self, xpos):
        """
        This function determines the x coordinate of the mouse and sets it to the middle of the paddle
        :param xpos:
        :return:
        """
        self.rect.centerx = xpos
