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
lostBG = pygame.image.load("images/face_lose.png").convert_alpha()
lostBG = pygame.transform.scale(lostBG, (800, 800))
screen.blit(lostBG, (0,0))

pygame.display.set_caption("You lost!")

font = pygame.font.SysFont('cambria', 60)
text_surface = font.render('You lost the game!', True, (black))
screen.blit(text_surface, (170,350))


while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()