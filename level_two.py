#kitchen

import pygame
from pygame.locals import *

# start of the dialogue for Kit Kat and Kai
    #Kit Kat is trying to cheer up Kai for school. Kit kat believes that it will be a good day, but Kai disagrees saying that it is just the usual mundane day.
    #Kit Kat goes over to the cereal and says that it will make Kai a bowl of Oreo-O's (his favorite)

import cereal_game
import level_two_outside
from movement import *

def text_objects(text, font):
    black = (0,0,0)
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    white = (255,255,255)
    textSurface = font.render(text, True, white)
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

    truevar = True
    clock = pygame.time.Clock()

    clock.tick(180)

    pygame.init()


    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))


    player = Cat()
    table = Wall((400,400))
    full_kitchen = pygame.image.load("pics/lvl-bgs/full_kitchen.png").convert()
    full_kitchen = pygame.transform.scale(full_kitchen, (width,height))

    kaicon = pygame.image.load("KAI/uh2.png")
    kaicon = pygame.transform.scale(kaicon, (100,130))

    cereal = pygame.image.load("pics/lvl-bgs/cereal.png")
    cereal = pygame.transform.scale(cereal, (60,78))
    test_rect2 = cereal.get_rect()

    beforekitchentext = pygame.font.Font('fonts/arcade.ttf', 50)
    TextSurf, TextRect = text_objects("Kai", beforekitchentext)
    TextRect.center = (100,80)

    kitkat_thought_text = pygame.font.Font('fonts/cambria.ttf', 20)
    TextSurf1, TextRect1 = text_objects("Oops, we need to do something first!", kitkat_thought_text)

    text_box = pygame.image.load("pics/teal_rect.png")
    text_box.set_alpha(200)
    text_box = pygame.transform.scale(text_box, (width,150))

    dialogue = pygame.font.Font('fonts/livvic/livvic-medium.ttf', 20)

    TextSurf_n, TextRect_n = text_objects2("Press enter to continue.", dialogue)
    TextRect_n.center = (275,80)

    didplaycereal = False
    next = 0

    player.rect.x = 1000

    player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")

    while truevar:
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        cerealRectPos = (520,126,60,78)
        cerealRect = pygame.draw.rect(screen, white, cerealRectPos)

        rectangle = pygame.draw.rect(screen, (0,0,0), table)
        screen.blit(full_kitchen, (0,0))
        key = pygame.key.get_pressed()

        screen.blit(TextSurf,TextRect) #kai

        screen.blit(kaicon,(-400,100))

        #DIALOGUE GOES HERE
        if key[pygame.K_RETURN]:
            dialoguebarPos = (90,380,1000,300)
            dialoguebar = pygame.draw.rect(screen, white, dialoguebarPos)

        screen.blit(cereal, (520,126))
        screen.blit(text_box, (0,0))
        screen.blit(TextSurf,TextRect)

        if didplaycereal == False:
            if click[0] == 1 and cerealRect.collidepoint(mouse):
                didplaycereal = True
                cereal_game.cerealgame()
                continue

        screen.blit(player.image, player.rect)
        player.update()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2)
            player.image = pygame.image.load("KIT_KAT/kitkat_left2.png")
        if key[pygame.K_RIGHT]:
            player.move(2)
            player.image = pygame.image.load("KIT_KAT/kitkat_right2.png")
        if key[pygame.K_UP]:
            player.jump()

        if didplaycereal == True:
            if player.rect.x < -100:
                level_two_outside.leveltwooutside()

        # if didplaycereal == False:
        #     if player.rect.x < -100:
        #         kitkat_thoughtpos = (player.rect.x + 75, player.rect.y - 100, 100,75)
        #         kitkat_thought = pygame.draw.ellipse(screen, white, kitkat_thoughtpos)
        #
        #         TextRect1.center = (player.rect.x - 200, player.rect.y - 50)
        #         screen.blit(TextSurf1,TextRect1)

# needs to have dialogue for Kai and Kit Kat after the cereal game

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit(0)

leveltwo()
