import random
import pygame

def drawSnake(snake):
    for coord in snake.coordinates:
        x = coord['x'] * Grid_Size
        y = coord['y'] * Grid_Size
        wormSegmentRect = pygame.Rect(x, y, Grid_Size, Grid_Size)
        pygame.draw.rect(Surfingdisplay, Black, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, Grid_Size - 8, Grid_Size - 8)
        pygame.draw.rect(Surfingdisplay, Black, wormInnerSegmentRect)

def drawApple(x, y, Grid_Size, Grid_Size):
    appleRect = pygame.Rect(x, y, Grid_Size, Grid_Size)
    pygame.draw.rect(Surfingdisplay, Red, appleRect)

def eat_apple(apple_list, snake): 
    head_location = {'x':snake.x, "y":snake.y}
    if head_location in apple_list:
        apple_list.remove(head_location)

    # generate new apple, redo if in apple_list or snake coordinates
    new_apple = getRandomLocation()
    while new_apple in apple_list or new_apple in snake.coordinates:
        new_apple = getRandomLocation()
    

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
    overRect = Surfing2.get_rect(midtop=(FrameWidth / 2, gameRect.height + 30)) 

    Surfingdisplay.blit(Surfing1, gameRect)
    Surfingdisplay.blit(Surfing2, overRect)
    showKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    pygame.draw.rect(Surfingdisplay, Red, appleRect)
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
        pygame.draw.line(Surfingdisplay, GRAY_DARK, (x, 0), (x, FrameHeight))
    for y in range(0, FrameHeight, Grid_Size):  # draw horizontal lines
        pygame.draw.line(Surfingdisplay, GRAY_DARK, (0, y), (FrameWidth, y))

        
def terminate():
    pygame.quit()
    sys.exit()