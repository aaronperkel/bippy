#Aaron Perkel
#Untitled Game V1.0.0 (02/17/21 19:41:27PM)

#GAME
#MENU:
#   Title
#   Start Game
#CUTSCENE:
#   camera pans in to two lovers, female gets taken
#   skip button
#GAME STARTS:
    #jump to avoid obsticales
    #get to the end to save her


import pygame as pg, random, sys

def closeWindow():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


title = False
game = True

screenW, screenH = 600, 400
white = (255, 255, 255)
blue = (0, 0, 255)

isJump = False
v = 8
m = 2
yLoc = 330

screen = pg.display.set_mode((screenW, screenH))
pg.display.set_caption('Untitled Game V1.0.0')
screen.fill(white)
pg.display.update()

while title:
    closeWindow()
    screen.fill((74, 116, 255))
    keys = pg.key.get_pressed()


    pg.display.update()

while game:
    closeWindow()
    screen.fill(white)
    keys = pg.key.get_pressed()

    if not isJump:
        if keys[pg.K_SPACE]:
            isJump = True

    if isJump:
        yLoc -= (1/2)*m*(v**2)
        v -= 1
        if v < 0:
            m = -2
        if v == -9:
            isJump = False
            v = 8
            m = 2

    pg.time.delay(10)

    pg.draw.rect(screen, blue, (275, yLoc, 50, 50), 2)

    pg.display.update()
