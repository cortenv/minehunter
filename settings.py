import pygame
import sys
pygame.font.init()
from main import getWin
from main import getLost

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
screenSize = (800, 800)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Spiel einstellungen:")

font = pygame.font.SysFont('arial',35)
text = font.render('Spielfeldgrösse:' , True , white)
text = font.render('9x9' , True , white)
text = font.render('14x14' , True , white)
text = font.render('20x20' , True , white)
text = font.render('Recursion an oder aus?' , True , white)


#class Button():
    #def __init__(self):


#button = Button()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()