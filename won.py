import pygame
import sys

pygame.init()
pygame.font.init()
pygame.font.get_fonts


white = (255, 255, 255)
black = (0, 0, 0)
screenSize = (800, 800)
screen = pygame.display.set_mode(screenSize)
screen.fill(white)
winBG = pygame.image.load("images/face_win.png").convert_alpha()
winBG = pygame.transform.scale(winBG, (800, 800))
screen.blit(winBG, (0,0))

pygame.display.set_caption("You won!")

font = pygame.font.SysFont('cambria', 60)
text_surface = font.render('You won the game!', True, (black))
screen.blit(text_surface, (170,350))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()