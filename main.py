import pygame
from common import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX))
clock = pygame.time.Clock()
running = True
dt: int = 0

while running:

    ######################
    ### PART 1: UPDATE ###
    ######################

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO: update code goes here

    ######################
    ### PART 2: UPDATE ###
    ######################
    
    # TODO: drawing code goes here

    screen.fill(COLOR_BLACK) # clear the screen

    pygame.display.flip()

    dt = clock.tick(FPS)  # limits FPS to 60

pygame.quit()