import sys
import numpy as np
import random

import pygame
from pygame.locals import *

from Snake import Snake

FrameWidth = 800
FrameHeight = 500
Grid_Size = 20

Grid_W = int(FrameWidth / Grid_Size)
Grid_H = int(FrameHeight / Grid_Size)  

HEAD = 0

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Gold = (255, 215, 0)
Blue = (0, 0, 255)
Gray = (40, 40, 40)
RedPink = (249, 91, 91)

BackgroundCOLOR = Gold

def drawSnake(snake, Grid_Size=Grid_Size):
    for coord in snake.coordinates:
        x = coord['x'] * Grid_Size
        y = coord['y'] * Grid_Size
        wormSegmentRect = pygame.Rect(x, y, Grid_Size, Grid_Size)
        pygame.draw.rect(Surfingdisplay, Black, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, Grid_Size - 8, Grid_Size - 8)
        pygame.draw.rect(Surfingdisplay, Black, wormInnerSegmentRect)

def drawApple(apple_list, Grid_Size=20):
    for apple in apple_list:
        appleRect = pygame.Rect(apple['x']*Grid_Size, apple['y']*Grid_Size, Grid_Size, Grid_Size)
        pygame.draw.rect(Surfingdisplay, Red, appleRect)

def eat_apple(apple_list, snake): 
    temp = apple_list
    head_location = {'x':snake.x, "y":snake.y}
    
    if head_location in apple_list:
        temp.remove(head_location)
        
        # generate new apple, redo if in apple_list or snake coordinates
        new_apple = getRandomLocation()
        while new_apple in apple_list or new_apple in snake.coordinates:
            new_apple = getRandomLocation()
    
        temp.append(new_apple)

        snake.change_length()
        snake.set_eating()
            
    return temp
    
def getRandomLocation(Grid_W=40, Grid_H=25):
    return {'x': random.randint(0, Grid_W - 1), 'y': random.randint(0, Grid_H - 1)}

def showKeyMsg():
    FONT_BASIC = pygame.font.Font('freesansbold.ttf', 18)
    keySurf = FONT_BASIC.render('Press any key to begin!', True, RedPink)
    keyRect = keySurf.get_rect(topleft = (FrameWidth-210, FrameHeight-30))
    Surfingdisplay.blit(keySurf, keyRect)
    
        
def KeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUp_showing = pygame.event.get(KEYUP)
    if len(keyUp_showing) == 0:
        return None
    if keyUp_showing[0].key == K_ESCAPE:
        terminate()
    return keyUp_showing[0].key

# check while true loop
def showStartScreen():
    Font_title = pygame.font.Font('freesansbold.ttf', 60)
    startSurf = Font_title.render("Let's Play Greedy Snake!", True, RedPink) 
    Surfingdisplay.fill(BackgroundCOLOR) 
    startRect = startSurf.get_rect(center=(FrameWidth/2, FrameHeight/2)) 
    Surfingdisplay.blit(startSurf, startRect) 
    showKeyMsg() #show the msg on screen
    pygame.display.update()
    
    while True:
        if KeyPress():
            pygame.event.get()
            return

def showGameOverScreen():
    Font_gameOver = pygame.font.Font('freesansbold.ttf', 100)
    Surfing1 = Font_gameOver.render('You', True, White) 
    Surfing2 = Font_gameOver.render('Lose', True, White) 
    gameRect = Surfing1.get_rect(midtop=(FrameWidth / 2, 10)) 
    overRect = Surfing2.get_rect(midtop=(FrameWidth / 2, gameRect.height + 20)) 

    Surfingdisplay.blit(Surfing1, gameRect)
    Surfingdisplay.blit(Surfing2, overRect)

    showKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    KeyPress()
    
    while True:
        if KeyPress():
            pygame.event.get()
            return 

def drawScore(score):
    scoreSurfing = FONT_BASIC.render('Score: %s' % (score), True, White)
    scoreRect = scoreSurfing.get_rect()
    scoreRect.topleft = (FrameWidth - 120, 10)
    Surfingdisplay.blit(scoreSurfing, scoreRect)
    
def drawGrid():
    for x in range(0, FrameWidth, Grid_Size):  # draw vertical lines
        pygame.draw.line(Surfingdisplay, Gray, (x, 0), (x, FrameHeight))
    for y in range(0, FrameHeight, Grid_Size):  # draw horizontal lines
        pygame.draw.line(Surfingdisplay, Gray, (0, y), (FrameWidth, y))

        
def terminate():
    pygame.quit()
    sys.exit()


def rungame(snake, num_apples=20):
    
    
    # create a group of apples and append to list
    apple_list = []
    apple_list = [getRandomLocation(Grid_W, Grid_H) for i in range(num_apples)]    
    
    
    # Main game loop
    while snake.alive:
        for event in pygame.event.get():
        
            # if quit, then terminate
            if event.type == QUIT:
                terminate()
                
            # if direction key is pressed, change direction if not opposite direction
            elif event.type == KEYDOWN:
                if event.key == K_LEFT :
                    snake.change_direction('left')
                elif event.key == K_RIGHT:
                    snake.change_direction('right')
                elif event.key == K_UP:
                    snake.change_direction('up')
                elif event.key == K_DOWN:
                    snake.change_direction('down')

            # if space is pressed, the snake speeds up
                elif event.key == K_SPACE:
                    snake.change_speed(5)
        
        Surfingdisplay.fill(BackgroundCOLOR)
        drawGrid()
        apple_list = eat_apple(apple_list, snake)
        
        snake.move_to_next_position()
        
        if not snake.alive:
            return
            
        drawSnake(snake)
        
        drawApple(apple_list,20)
        
        drawScore(snake.length - 3)
        
        pygame.display.update()
        Snakespeed_CLOCK.tick(snake.speed)    
        
        
                
def main():
    FrameWidth = 800
    FrameHeight = 500
    Grid_Size = 20

    Grid_W = int(FrameWidth / Grid_Size)
    Grid_H = int(FrameHeight / Grid_Size)  

    HEAD = 0

    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Gold = (255, 215, 0)
    Blue = (0, 0, 255)
    Gray = (40, 40, 40)
    RedPink = (249, 91, 91)

    BackgroundCOLOR = Gold 
    global Snakespeed_CLOCK, Surfingdisplay, FONT_BASIC

    pygame.init()
    Snakespeed_CLOCK = pygame.time.Clock()
    Surfingdisplay = pygame.display.set_mode((FrameWidth, FrameHeight))
    FONT_BASIC = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake')

    showStartScreen()
    while True:
        snake = Snake(Grid_W, Grid_H) #parameters
        rungame(snake)
        showGameOverScreen()


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass

