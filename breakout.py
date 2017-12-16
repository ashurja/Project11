# Jamshed Ashurov
# 12/16/2017
# breakout.py
# This is the main file of the program. It imports all the classes to make the breakout game

import pygame, sys
from pygame.locals import *
import ball
import brick
import paddle


def main():
    pygame.init()
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_X_OFFSET = 0
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    NUM_TURNS = 3
    mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Jamshed's Innovative Breakout")
    bricksGroup = pygame.sprite.Group()
    paddleGroup = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()
    Turns = 0
    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    xposition = BRICK_X_OFFSET
    yposition = BRICK_Y_OFFSET
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN]
    for colour in colors:          # Loop that creates the bricks
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                myBrick = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, colour, mainsurface)
                myBrick.rect.x = xposition
                myBrick.rect.y = yposition
                xposition += BRICK_WIDTH + BRICK_SEP
                mainsurface.blit(myBrick.image, myBrick.rect)
                bricksGroup.add(myBrick)
            xposition = 0
            yposition += BRICK_HEIGHT + BRICK_SEP
        xposition = 0

    # Creates and positions the paddle
    myPaddle = paddle.Paddle(WHITE, mainsurface)
    myPaddle.rect.y = APPLICATION_HEIGHT-PADDLE_Y_OFFSET
    mainsurface.blit(myPaddle.image, myPaddle.rect)
    paddleGroup.add(myPaddle)

    # Creates and positions the ball
    myBall = ball.Ball(WHITE, mainsurface)
    myBall.rect.x = APPLICATION_WIDTH/2
    myBall.rect.y = APPLICATION_HEIGHT/2
    ballGroup.add(myBall)

    # Loads and plays the music
    pygame.mixer.music.load("velikolepnyj_vek_velikolepnaya_pesnya_(mp3co.co).mp3")
    pygame.mixer.music.play(-1)

    while True:
        # When the ball hits the bottom side, positions the ball back to the middle of the screen and adds the turn.
        if myBall.rect.bottom > APPLICATION_HEIGHT:
            myBall.rect.x = APPLICATION_WIDTH / 2
            myBall.rect.y = APPLICATION_HEIGHT / 2
            Turns = Turns + 1

        # When the number of turns reaches three, the game over message appears.
        if Turns == NUM_TURNS:
            mainsurface.fill(BLACK)
            text = pygame.font.SysFont("Helvetica", 50)
            textLabel = text.render(str("Game over"), 1, WHITE)
            textLabel2 = text.render(str("You lost"), 1, WHITE)
            mainsurface.blit(textLabel, (120, 150))
            mainsurface.blit(textLabel2, (135, 200))
            pygame.display.update()
            pygame.time.wait(10)
            pygame.quit()
            pygame.time.wait(2000)
            sys.exit()

        # When the last brick disappears the winning message appears.
        elif len(bricksGroup.sprites()) == 0:
            mainsurface.fill(BLACK)
            text = pygame.font.SysFont("Helvetica", 25)
            textLabel = text.render(str("Congratulations!"), 1, WHITE)
            textLabel2 = text.render(str("You won the game."), 1, WHITE)
            mainsurface.blit(textLabel, (150, 150))
            mainsurface.blit(textLabel2, (150, 200))
            pygame.display.update()
            pygame.time.wait(10)
            pygame.quit()
            pygame.time.wait(2000)
            sys.exit()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Makes the breakout game
        else:
            mainsurface.fill(BLACK)
            for myBrick in bricksGroup:
                mainsurface.blit(myBrick.image, myBrick.rect)

            myPaddle.move(pygame.mouse.get_pos()[0])
            mainsurface.blit(myPaddle.image, myPaddle.rect)
            myBall.move()
            myBall.collidePaddle(paddleGroup)
            myBall.collide(bricksGroup)
            mainsurface.blit(myBall.image, myBall.rect)
            pygame.display.update()
main()
