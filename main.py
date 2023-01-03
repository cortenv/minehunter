import pygame
import os

class Board():
    def __init__(self, size):
        self.size = size
        self.setBoard()

    def setBoard(self):
        self.board = []
        for row in range (self.size[0]):
            row = []
            for col in range(self.size[1]):
                piece = None
                row.append(piece)
            self.board.append(row)

    def getSize(self):
        return self.size
            
class Game():
    def __init__(self, board, screenSize):
        self.board = board
        self.screenSize = screenSize
        self.pieceSize = self.screenSize[0] // self.board.getSize()[1], self.screenSize[1] // self.board.getSize()[0]
        self.loadImages()

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load("images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                image = self.images["tile"]
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1] 
        

size = (9, 9)
board = Board(size)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()

while True:
    pygame.display.update()