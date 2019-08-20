# Things to do here:
# Make scene function
# Have Kai lay on the bed
# Kit Kat is movable by wasd or arrow keys and can jump
# Collision detection works
# Interacting with the door will exit to the kitchen
# Make furniture interactive (i.e. clicking on the cat door will send Kit Kat to closet)
import pygame
from pygame.locals import *
import transitions
from transitions import *
import random

# import start_menu
from movement import Cat
from movement import Wall
from itertools import chain

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def levelone ():

    pygame.init() #take this out later

    flags = FULLSCREEN | DOUBLEBUF

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)

    #defining screen
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height),flags)
    transitions.init ( screen, width, height )

    truevar = True
    DoorOpen = false
    clock = pygame.time.Clock()
    jumps = 0

    player = Cat()
    bedroom = pygame.image.load("pics/lvl-bgs/full_bedroom2.png").convert()
    bed = Wall((50, 400))

    while truevar:
        rectangle = pygame.draw.rect(screen, (0,0,0), bed)
        screen.blit(bedroom, (0,0))

        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
        if key[pygame.K_RIGHT]:
            player.move(2)
        if key[pygame.K_UP]:
            player.jump()

        print (player.jumpdone)
        if player.jumpdone== 10
            DoorOpen = true
        # if runSecondTime == True:
        #     if click[0] == 1 and goBackButton.collidepoint(mouse):
        #
        #         start_menu.game_intro()
        #         truevar = False

        #defining texts
        #button text
        # buttonText = pygame.font.Font('fonts/Roboto-Thin.ttf', 25)
        # TextSurf3, TextRect3 = text_objects("go back", buttonText)
        # TextRect3.center = (1050,125)
        #
        #speech bubble text
        speechText = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

        TextSurf4, TextRect4 = text_objects("Jump on Kai to wake them up!", speechText)
        TextRect4.center = (900,80)
        screen.blit(TextSurf4,TextRect4)

        screen.blit(player.image, player.rect)

        clock.tick(150)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   pygame.quit()
                   exit(0)

#take this out later
levelone()
