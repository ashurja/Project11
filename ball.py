# Jamshed Ashurov
# 01/11/2018
# ball.py
# This file creates the ball, functions to move it, and functions for collisions

import pygame
import random


# Creates the Call class of the game. Uploads the image of the ball and sets up the speed of the ball
class Ball(pygame.sprite.Sprite):

    def __init__(self, mainsurface):
        super().__init__()
        self.RADIUS = 10
        self.mainsurface = mainsurface
        self.image = pygame.image.load("download (1).jpeg")
        self.rect = self.image.get_rect()
        self.speedx = random.randint(4, 7)
        self.speedy = random.randint(5, 7)

    def move(self):
        """
        The function determines the speed of the ball and the x and y direction speeds when the ball hits the top
        and side walls.
        :return:
        """
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        if self.rect.right > self.mainsurface.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.top < 0:
            self.speedy = -self.speedy

    def collidePaddle(self, paddleGroup):
        """
        This function determines the y coordinate speed when the ball collides with the paddle
        :param paddleGroup:
        :return:
        """
        if pygame.sprite.spritecollide(self, paddleGroup, False):
            self.speedy = -self.speedy

    def collide(self, brickGroup):
        """
        This function determines the y coordinate speed when the ball collides with the brick
        :param brickGroup:
        :return:
        """
        if pygame.sprite.spritecollide(self, brickGroup, True):
            self.speedy = -self.speedy