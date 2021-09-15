#Aaron Perkel
#Untitled Game V1.0.1 (02/18/21 10:58:47PM)

#TODO
#MENU:
#   Start Game
#CUTSCENE:
#   camera pans in to two lovers, female gets taken
#   skip button
#GAME STARTS:
    #jump to avoid obsticales
    #get to the end to save her


import pygame as pg, random, sys
pg.init()

def closeWindow(): # 'X' button to close window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


title = True # booleans
game = False
isJump = False
enterScreen = False

screenW, screenH = 600, 400 # window size and colors
white = (255, 255, 255)
blue = (74, 116, 255)

button = pg.image.load('button.png') # images
buttonPress = pg.image.load('buttonPress.png')
man = pg.image.load('man.png')
man = pg.transform.scale(man, (50, 50))
bg = pg.image.load('bg.png')

yLoc = 330 # man yLoc
xLoc = -50 # man xLoc
v, m = 8, 2 # velocity and mass of square
buttonX, buttonY = 210, 275 # button location

screen = pg.display.set_mode((screenW, screenH)) # window
pg.display.set_caption('Untitled Game V1.0.1') # window title

font = pg.font.Font('font.ttf', 24) # font
play = font.render('PLAY!', True, 0) # play text
title = pg.font.Font('font.ttf', 114).render('BIPPY', True, (236,180,28)) # title text
name = pg.font.SysFont(None, 24).render('Aaron Perkel', True, 0) # name text

while title:
    closeWindow() # 'X' to close window
    screen.fill(blue)
    keys = pg.key.get_pressed() # list of pressed keys
    mouseX, mouseY = pg.mouse.get_pos() # mouse position

    screen.blit(bg, (0, 0)) # background image
    screen.blit(title, (180, 80)) # title
    screen.blit(name, (10, 380)) # name 

    # 'box' around button
    if mouseX > buttonX and mouseX < buttonX + 180 and mouseY > buttonY and mouseY < buttonY + 44:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND) # hand cursor on button
        screen.blit(buttonPress, (buttonX, buttonY)) # button pressed image
        screen.blit(play, (buttonX + 62, buttonY + 8)) # text shift to press
        if pg.mouse.get_pressed()[0]: # left click
            title = False # plays game
            enterScreen = True
    else:
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW) # regular cursor
        screen.blit(button, (buttonX, buttonY)) # button unpressed image
        screen.blit(play, (buttonX + 62, buttonY + 6)) # play text

    pg.display.update()

while enterScreen:
    screen.fill((79, 232, 115))
    closeWindow()

    screen.blit(man, (xLoc, yLoc))

    xLoc += 4

    yLoc -= (1/2)*m*(v**2) # kenetic energy equation
    v -= 1 # slows velocity
    if v < 0: # at top of jump arc
        m = -2 # mass is 'negative' to fall
    if v == -9: # if on ground
        v, m = 8, 2 # reset velocity and mass

    pg.time.delay(30) # delay next jump

    if xLoc >= 290:
        xLoc = 290
        yLoc = 330
        enterScreen = False
        game = True

    pg.display.update()



while game:
    screen.fill((79, 232, 115))
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW) # regular cursor
    closeWindow() # 'X' to close window
    
    keys = pg.key.get_pressed() # list of pressed keys

    if not isJump: # if square is on ground
        if keys[pg.K_SPACE] or keys[pg.K_UP]: # if space is clicked
            isJump = True # jump

    if isJump: # if jumping
        yLoc -= (1/2)*m*(v**2) # kenetic energy equation
        v -= 0.6 # slows velocity
        if v < 0: # at top of jump arc
            m = -2 # mass is 'negative' to fall
        if yLoc >= 330: # stops at bottom of screen
            yLoc = 330
            isJump = False
            v, m = 8, 2

    if keys[pg.K_LEFT]:
        if xLoc >= 0:
            xLoc -= 8
    
    if keys [pg.K_RIGHT]:
        if xLoc <= screenW - 50:
            xLoc += 8

    pg.time.delay(10) # delay next jump

    screen.blit(man, (xLoc, yLoc)) # draws man

    pg.display.update()
