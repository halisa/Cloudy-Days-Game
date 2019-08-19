#kitchen

import pygame
from pygame.locals import *
import transitions
from transitions import *
import random

import start_menu

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def leveltwo ():

    # flags = FULLSCREEN | DOUBLEBUF

    #define colors
    black = (0,0,0)
    white = (255,255,255)
    red = (255,0,0)
    lightBlue = (180,180,225)
    darkBlue = (141,138,186)
    darkerBlue = (114,111,161)

    #defining screen
    width, height = 1200,600
    screen = pygame.display.set_mode((width, height))
    transitions.init ( screen, width, height )

    truevar = True
    clock = pygame.time.Clock()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()

    clock.tick(180)

    while truevar:
        kitchen = pygame.image.load("pics/lvl-bgs/kitchen.png").convert()
        kitchen = pygame.transform.scale(kitchen, (width,height))
        screen.blit(kitchen, (0,0))

        chair1 = pygame.image.load("pics/lvl-bgs/chair1.png")
        chair1 = pygame.transform.scale(chair1, (width,height))
        screen.blit(chair1, (0,0))

        chair2 = pygame.image.load("pics/lvl-bgs/chair2.png")
        chair2 = pygame.transform.scale(chair2, (width,height))
        screen.blit(chair2, (0,0))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit(0)
                elif event.key == K_KP_ENTER:
                    pygame.quit()
                    exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_img = event.pos

leveltwo()
