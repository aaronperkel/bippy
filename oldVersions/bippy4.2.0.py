#Aaron Perkel
#Bippy V4.2.0 (02/21/21 09:22:25PM)

#TODO:
#   make obstacle textures
#   make objects collidable
#   make progress bar

import pygame as pg, sys, time, math, random

screenW, screenH = 600, 400 # window size and colors
screen = pg.display.set_mode((screenW, screenH)) # window
pg.display.set_caption('Bippy V4.2.0') # window title
pg.init()

def closeWindow(): # 'X' button to close window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

class Object: # class to handle objects
    def __init__(self, inputScreen): # initialize class
        self.screen = inputScreen # screen
        self.xLoc = 660 # object xLoc
        self.fire1 = pg.image.load('fire1.png')
        self.fire1 = pg.transform.scale(self.fire1, (42, 50))
        self.fire2 = pg.image.load('fire2.png')
        self.fire2 = pg.transform.scale(self.fire2, (45, 50))
        self.fire3 = pg.image.load('fire3.png')
        self.fire3 = pg.transform.scale(self.fire3, (45, 50))
        self.pipe = pg.image.load('pipe.png')
        self.pipe = pg.transform.scale(self.pipe, (48, 96))

    def drawObject(self):
        choice = random.randint(1, 3)
        if choice == 1:
            screen.blit(self.fire1, (self.xLoc, 326))
        elif choice == 2:
            screen.blit(self.fire2, (self.xLoc, 326))
        else:
            screen.blit(self.fire3, (self.xLoc, 326))
        screen.blit(self.pipe, (self.xLoc - 2, 376))

    def moveObject(self):
        self.xLoc -= objSpeed # moves object left
        if self.xLoc <= -60: # if off left of screen
            self.xLoc = 660 # goes back to the right of screen

    def isCollided(self, inputX, inputY):
        a = inputX - self.xLoc
        b = inputY - 326
        c = math.sqrt(a*a + b*b)
        if c < 35:
            objects.remove(i)
            return True

titleScreen = True # booleans
gameScreen = False
isJump = False
enterScreen = False
endScreen = False
controlsScreen = False

def resetVars(): 
    global xLoc, yLoc, v, m, buttonX, buttonY, buttonX2, buttonY2, villainX, girlX
    global objSpeed, bgW, bgH, spaceX, spaceY, keyboardX, keyboardY, backX, backY
    global bg1XLoc, bg2XLoc, objects
    xLoc, yLoc = -50, 330 # man xLoc and yLoc
    v, m = 8, 2 # velocity and mass of object
    buttonX, buttonY = 210, 245 # button location
    buttonX2, buttonY2 = 210, 295
    villainX = 630 # villian xLoc
    girlX = 400 # fippy xLoc
    objSpeed = 6 # object and bg speed
    bgW, bgH = 644, 400 # bg width and height
    spaceX, spaceY = 100, 50 # space bar xLoc and yLoc
    keyboardX, keyboardY = 153, 170 # keyboard xLoc and yLoc
    backX, backY = 10, 10 # back button xLoc and yLoc
    bg1XLoc = 0 # bg image one xLoc
    bg2XLoc = bg1XLoc + bgW #bg image 2 xLoc
    objects = [] # list to hold objects
    objects.append(Object(screen)) # adds one object to list

resetVars()

button = pg.image.load('button.png') # images
buttonPress = pg.image.load('buttonPress.png')
man = pg.image.load('man.png')
man = pg.transform.scale(man, (50, 46))
bg = pg.image.load('bg.png')
girl = pg.image.load('girl.png')
girl = pg.transform.scale(girl, (54, 46))
villain = pg.image.load('villain.png')
villain = pg.transform.scale(villain, (41, 60))
bg1 = pg.image.load('bg1.png')
bg1 = pg.transform.scale(bg1, (bgW, bgH))
space = pg.image.load('space.png')
space = pg.transform.scale(space, (400, 100))
spacePress = pg.image.load('spacePress.png')
spacePress = pg.transform.scale(spacePress, (400, 100))
keyboard = pg.image.load('keyboard.png')
keyboard = pg.transform.scale(keyboard, (295, 100))
upPress = pg.image.load('upPress.png')
upPress = pg.transform.scale(upPress, (98, 49))
leftPress = pg.image.load('leftPress.png')
leftPress = pg.transform.scale(leftPress, (95, 100))
rightPress = pg.image.load('rightPress.png')
rightPress = pg.transform.scale(rightPress, (95, 100))

font = pg.font.Font('font.ttf', 24) # font
play = font.render('PLAY!', True, 0) # play text
controls = font.render('CONTROLS', True, 0) # controls text
title = pg.font.Font('font.ttf', 114).render('BIPPY', True, (236, 180, 28)) # title text
name = pg.font.SysFont(None, 24).render('Aaron Perkel', True, 0) # name text
fippy1 = font.render('Hey Bippy <3', True, 0) # speech lines
fippy2 = font.render('AHHH! HELP!', True, 0)
bippy1 = font.render('Hey Fippy <3', True, 0)
bippy2 = font.render('FIPPY WATCH OUT!', True, 0)
bippy3 = font.render('I\'LL SAVE YOU!', True, 0)
villain1 = font.render('I got you now Fippy!', True, 0)
go = pg.font.Font('font.ttf', 114).render('SAVE FIPPY!', True, (236, 180, 28)) # start text
end = font.render('TEMPORARY END SCREEN. PRESS \'r\' TO RESTART', True, 0) # end text
jumpText = font.render('JUMP - space bar or up arrow', True, 0) # jump instructions
moveText = font.render('MOVE - left or right arrow', True, 0) # move instructions
back = pg.font.Font('font.ttf', 18).render('BACK', True, 0)

while True:
    while titleScreen:
        closeWindow() # 'X' to close window
        screen.fill((74, 116, 255))
        mouseX, mouseY = pg.mouse.get_pos() # mouse position

        screen.blit(bg, (0, 0)) # background image
        screen.blit(title, (180, 80)) # title
        screen.blit(name, (10, 380)) # name 
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW) # regular cursor

        # 'box' around buttons
        if mouseX > buttonX and mouseX < buttonX + 180 and mouseY > buttonY and mouseY < buttonY + 44:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND) # hand cursor on button
            screen.blit(buttonPress, (buttonX, buttonY)) # button pressed image
            screen.blit(play, (buttonX + 62, buttonY + 8)) # text shift to press
            if pg.mouse.get_pressed()[0]: # left click
                titleScreen = False # plays game
                enterScreen = True
                startTime = time.time() # starts timer
        else:
            screen.blit(button, (buttonX, buttonY)) # button unpressed image
            screen.blit(play, (buttonX + 62, buttonY + 6)) # play text

        if mouseX > buttonX2 and mouseX < buttonX2 + 180 and mouseY > buttonY2 and mouseY < buttonY2 + 44:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND) # hand cursor on button
            screen.blit(buttonPress, (buttonX2, buttonY2)) # button pressed image
            screen.blit(controls, (buttonX2 + 44, buttonY2 + 8)) # text shift to press
            if pg.mouse.get_pressed()[0]: # left click
                titleScreen = False
                controlsScreen = True
        else:
            screen.blit(button, (buttonX2, buttonY2)) # button unpressed image
            screen.blit(controls, (buttonX2 + 44, buttonY2 + 6)) # controls text

        pg.display.update()

    while controlsScreen:
        screen.fill((89, 153, 255))
        mouseX, mouseY = pg.mouse.get_pos() # mouse position
        keys = pg.key.get_pressed() # list of pressed keys
        closeWindow() # 'X' to close window
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW) # regular cursor

        screen.blit(keyboard, (keyboardX, keyboardY)) # unpressed keyboard
        screen.blit(jumpText, (160, 300)) # jump instructions
        screen.blit(moveText, (173, 350)) # move instructions

        if mouseX > backX and mouseX < backX + 120 and mouseY > backY and mouseY < backY + 29:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND) # hand cursor on button
            screen.blit(pg.transform.scale(buttonPress, (120, 29)), (backX, backY)) # button pressed image
            screen.blit(back, (backX + 41, backY + 5))
            if pg.mouse.get_pressed()[0]: # left click
                titleScreen = True
                controlsScreen = False
        else:
            screen.blit(pg.transform.scale(button, (120, 29)), (backX, backY))
            screen.blit(back, (backX + 41, backY + 3))

        if keys[pg.K_SPACE]: # KEY ANIMATIONS
            screen.blit(spacePress, (spaceX, spaceY))
        else:
            screen.blit(space, (spaceX, spaceY))

        if keys[pg.K_UP]:
            screen.blit(upPress, (keyboardX + 99, keyboardY))
        if keys[pg.K_LEFT]:
            screen.blit(leftPress, (keyboardX, keyboardY))
        if keys[pg.K_RIGHT]:
            screen.blit(rightPress, (keyboardX + 200, keyboardY))

        pg.display.update()

    while enterScreen:
        screen.blit(bg1, (0, 0)) # background image
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW) # regular cursor
        closeWindow() # 'X' to close window

        screen.blit(man, (xLoc, yLoc)) # draws bippy
        screen.blit(girl, (girlX, 330)) # draws fippy
        screen.blit(villain, (villainX, 316)) # draws villain

        xLoc += 4 # moves bippy right

        yLoc -= (1/2)*m*(v**2) # kenetic energy equation
        v -= 1 # slows velocity
        if v < 0: # at top of jump arc
            m = -2 # mass is 'negative' to fall
        if yLoc >= 330: # if on ground
            yLoc = 330
            v, m = 8, 2 # reset velocity and mass

        pg.time.delay(30) # delay next jump

        if xLoc >= 150:
            endTime = time.time() # starts another timer
            difTime = endTime - startTime # time between times
            xLoc = 160
            yLoc = 330
            if difTime <= 2.9: # bippy first text
                screen.blit(fippy1, (360, 300))
            if difTime > 3.1 and difTime < 4.8: # fippy first text
                screen.blit(bippy1, (120, 300))
            if difTime > 3.7 and difTime < 5.3: # villain moves
                if villainX >= 454: # fippy's right side
                    villainX -= 4
            if difTime > 5 and difTime < 7.2: # bippy second text
                screen.blit(bippy2, (120, 300))
            if difTime > 5.3 and difTime < 6.4: # villain first text
                screen.blit(villain1, (villainX-80, 286)) 
            if difTime > 6.8: # villain takes fippy
                girlX = villainX - 54
                villainX += 4
                screen.blit(fippy2, (girlX-40, 300)) # fippy second text
            if difTime > 7.3: # bippy third text
                screen.blit(bippy3, (120, 300))
            if girlX > screenW + 65: # starts game
                enterScreen = False
                gameScreen = True
                v, m = 4, 5
                startTime = time.time() # starts timer for next while loop

        pg.display.update()

    while gameScreen:
        endTime = time.time() # starts timer for text              
        difTime = endTime - startTime # time between enterScreen tmer and gameScreen timer
        
        if bg1XLoc <= -bgW: # if first bg is off screen
            bg1XLoc = bg2XLoc + (bgW-2) # move to end of second image
        else:
            bg1XLoc -= objSpeed # move bg left
        if bg2XLoc <= -bgW: # if second bf is off screen
            bg2XLoc = bg1XLoc + (bgW-2) # move to the end of first image
        else:
            bg2XLoc -= objSpeed # move bg left

        # if objSpeed < 10:
        #     objSpeed += 0.005

        screen.blit(bg1, (bg1XLoc, 0)) # draws bg 1
        screen.blit(bg1, (bg2XLoc, 0)) # draws bg 2

        closeWindow() # 'X' to close window

        if difTime <= 3: # title               
            screen.blit(go, (50, 50)) # draws text       
        
        keys = pg.key.get_pressed() # list of pressed keys

        if not isJump: # if object is on ground
            if keys[pg.K_SPACE] or keys[pg.K_UP]: # if space or up arrow is pressed
                isJump = True # jump

        if isJump: # if jumping
            yLoc -= (1/2)*m*(v**2) # kenetic energy equation
            v -= 0.4 # slows velocity
            if v < 0: # at top of jump arc
                m = -5 # mass is 'negative' to fall
            if yLoc >= 330: # stops at bottom of screen
                yLoc = 330
                isJump = False
                v, m = 4, 5

        if keys[pg.K_LEFT]: # left arrow
            if xLoc >= 0: # keeps from going off left of screen
                xLoc -= 8
        
        if keys [pg.K_RIGHT]: # right arrow
            if xLoc <= screenW - 50: # keeps from going off right of screen
                xLoc += 8

        pg.time.delay(20) # delay next jump

        screen.blit(man, (xLoc, yLoc)) # draws man

        for i in objects:
            i.drawObject()
            i.moveObject()
            if i.isCollided(xLoc, yLoc):
                gameScreen = False
                endScreen = True

        pg.display.update()

    while endScreen:
        keys = pg.key.get_pressed() # list of pressed keys
        screen.fill((79, 112, 239))
        closeWindow()

        if keys[pg.K_r]:
            resetVars()
            endScreen = False
            titleScreen = True

        screen.blit(end, (50, 50))

        pg.display.update()