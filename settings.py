import pygame
import sys
#pygame.font.init()
#from main import getWin
#from main import getLost

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
screenSize = (800, 800)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Spiel einstellungen:")

font = pygame.font.SysFont('arial',35)
text = font.render('Spielfeldgrösse:' , True , white)
text = font.render('5x5' , True , white)
text = font.render('9x9' , True , white)
text = font.render('20x20' , True , white)
text = font.render('Recursion an oder aus?' , True , white)


#class Button():
    #def __init__(self):


#button = Button()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()