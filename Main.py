import pygame
from Dictionary import *
from Tile import *
from WordUtils import *


#set up pygame
pygame.init()
framerate = 120
frameCount = 0
secondsPassed = 0
size = (width, height) = (1280, 720)
screen = pygame.display.set_mode(size)

#vars
midX = width/2
midY = height/2
white = (255,255,255)
black = (0,0,0)

#initialize the clock instance which will regulate framerate
Clock = pygame.time.Clock()

#font for rendering text
Font = pygame.font.Font(None, 36)



utils = WordUtils(Dictionary('dict.txt'))
tl = utils.getTileList(rand=False)
go = False

#t = Tile('a')


#GAME LOOP. This will run every frame until the program is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit(); sys.exit();

    #the screen must be erased every frame, the additional
    #elements are then redrawn over the white surface after their
    #positions are recalculated. This creates the illusion of motion
    screen.fill(white)

    #limit framerate
    ms = Clock.tick(framerate)

    #increment frame count and track seconds passed
    frameCount += 1
    if frameCount % framerate == 0: secondsPassed += 1
    
    #generates the info text labels. These must be
    #in multiple labels because the font renderer
    #cannot handle newline characters
    fpsText = ("FPS: "+str(int(Clock.get_fps())))
    fpsLabel = Font.render(fpsText, 1, black)
    timeText = ("Time: "+str(secondsPassed))
    timeLabel = Font.render(timeText, 1, black)


    #HANDLE KB INPUT
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            tl = utils.getTileList(rand=False)
            go = True
        elif event.key == pygame.K_2:
            tl = utils.getTileList(rand=True)
            go = True

    if go:
        for t in tl:
            t.update()
            t.draw(screen)

    

    screen.blit(fpsLabel, (0,0))
    screen.blit(timeLabel, (0,25))

    #update the screen
    pygame.display.flip()

