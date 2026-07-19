import pygame

#################
### game info ###
#################

SCREEN_WIDTH_PX: int = 1600
SCREEN_HEIGHT_PX: int = 900
SCREEN_RECT: pygame.Rect = pygame.Rect(0, 0, SCREEN_WIDTH_PX, SCREEN_HEIGHT_PX)
FPS: int = 60

##############
### colors ###
##############

# https://html-color.codes/
COLOR_RED           = pygame.Color(255,   0,   0)
COLOR_MAROON        = pygame.Color(128,   0,   0)
COLOR_BROWN         = pygame.Color(165,  42,  42)
COLOR_TAN           = pygame.Color(210, 180, 140)
COLOR_ORANGE        = pygame.Color(255, 165,   0)
COLOR_PEACH         = pygame.Color(255, 218, 185)
COLOR_GOLD          = pygame.Color(255, 215,   0)
COLOR_YELLOW        = pygame.Color(255, 255,   0)
COLOR_LIME          = pygame.Color(0,   255,   0)
COLOR_OLIVE         = pygame.Color(128, 128,   0)
COLOR_GREEN         = pygame.Color(  0, 128,   0)
COLOR_TEAL          = pygame.Color(  0, 128, 128)
COLOR_CYAN          = pygame.Color(  0, 255, 255)
COLOR_BLUE          = pygame.Color(  0,   0, 255)
COLOR_BLUE_MEDIUM   = pygame.Color(  0,   0, 205)
COLOR_NAVY          = pygame.Color(  0,   0, 128)
COLOR_PURPLE        = pygame.Color(128,   0, 128)
COLOR_MAGENTA       = pygame.Color(255,   0, 255)
COLOR_PINK          = pygame.Color(255, 192, 203)
COLOR_GRAY_DARK     = pygame.Color(128, 128, 128)
COLOR_GRAY_LIGHT    = pygame.Color(211, 211, 211)
COLOR_GRAY_MEDIUM   = pygame.Color(169, 169, 169)
COLOR_SILVER        = pygame.Color(192, 192, 192)
COLOR_WHITE         = pygame.Color(255, 255, 255)
COLOR_BLACK         = pygame.Color(  0,   0,   0)