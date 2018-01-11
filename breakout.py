# Jamshed Ashurov
# 01/11/2018
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
    GREY = (41, 41, 41)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    t = 0
    z = 1
    # 10 columns to put the images
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []
    column8 = []
    column9 = []
    column10 = []
    columns = [column1, column2, column3, column4, column5, column6, column7, column8, column9, column10]

    # This code starts with (0, 1) then goes on to (10, 10) inserting 10 images per column
    for column in columns:
        for y in range(10):
            for x in range(t, z):
                name = "images/" + str(x) + "_" + str(y) + ".jpg"
                column.append(name)
        t += 1
        z += 1

    xposition = BRICK_X_OFFSET
    yposition = BRICK_Y_OFFSET
    # For every image in the column group, starts in the initial position of (0, 70), then moves down the column with
    # the space distance of 4 + the height of the brick(8). Then it start with x as 4 + width of the brick(36.4) and
    # y as 70 and again moves down the column. The process repeats 10 times.
    for column in columns:
        for columna in column:
            myBrick = brick.Brick(columna)
            myBrick.rect.x = xposition
            myBrick.rect.y = yposition
            yposition += BRICK_HEIGHT + BRICK_SEP
            mainsurface.blit(myBrick.image, myBrick.rect)
            bricksGroup.add(myBrick)
        yposition = BRICK_Y_OFFSET
        xposition += BRICK_WIDTH + BRICK_SEP

    # Creates and positions the paddle
    myPaddle = paddle.Paddle(mainsurface)
    myPaddle.rect.y = APPLICATION_HEIGHT-PADDLE_Y_OFFSET
    mainsurface.blit(myPaddle.image, myPaddle.rect)
    paddleGroup.add(myPaddle)

    # Creates and positions the ball
    myBall = ball.Ball(mainsurface)
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
            pygame.time.wait(300)
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
            mainsurface.fill(GREY)
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
