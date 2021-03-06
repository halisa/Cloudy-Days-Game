import pygame
from pygame.locals import *

class Cat (pygame.sprite.Sprite):
    def __init__(self):
        super(Cat, self).__init__()
        self.image = pygame.image.load("pics/bird1.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 400 #change y position
        self.radius = int(self.rect.width / 2)

    def move(self, dx, dy):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        # for wall in walls:
        #     if self.rect.colliderect(wall.rect):
        #         if dx > 0: # Moving right; Hit the left side of the wall
        #             self.rect.right = wall.rect.left
        #         if dx < 0: # Moving left; Hit the right side of the wall
        #             self.rect.left = wall.rect.right
        #         if dy > 0: # Moving down; Hit the top side of the wall
        #             self.rect.bottom = wall.rect.top
        #         if dy < 0: # Moving up; Hit the bottom side of the wall
        #             self.rect.top = wall.rect.bottom

class Player(object):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("pics/bird1.png")
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(
        center = (25,25)
        )
        self.rect = pygame.Rect(32, 32, 16, 16)


    def move(self, dx, dy):

        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # # If you collide with a wall, move out based on velocity
        # for wall in walls:
        #     if self.rect.colliderect(wall.rect):
        #         if dx > 0: # Moving right; Hit the left side of the wall
        #             self.rect.right = wall.rect.left
        #         if dx < 0: # Moving left; Hit the right side of the wall
        #             self.rect.left = wall.rect.right
        #         if dy > 0: # Moving down; Hit the top side of the wall
        #             self.rect.bottom = wall.rect.top
        #         if dy < 0: # Moving up; Hit the bottom side of the wall
        #             self.rect.top = wall.rect.bottom

# while running:
#
#     clock.tick(60)
    #
    # for e in pygame.event.get():
    #     if e.type == pygame.QUIT:
    #         running = False
    #     if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
    #         running = False
    #
    # # Move the player if an arrow key is pressed
    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT]:
    #     player.move(-3, 0, walls)
    # if key[pygame.K_RIGHT]:
    #     player.move(3, 0, walls)
    # if key[pygame.K_UP]:
    #     player.move(0, -3, walls)
    # if key[pygame.K_DOWN]:
    #     player.move(0, 3, walls)
    #
    # # Just added this to make it slightly fun ;)
    # # if player.rect.colliderect(end_rect):
    # #     raise SystemExit, "You win!"
    #
    # # making cat move
    # # pressed_keys = pygame.key.get_pressed()
    # # player.update(pressed_keys)
    #
    # # Draw the scene
    # screen.fill((0, 0, 0))
    # for wall in walls:
    #     pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    # # pygame.draw.rect(screen, (255, 200, 0), player.rect)
    # screen.blit(player.image, player.rect)
    # pygame.display.flip()
