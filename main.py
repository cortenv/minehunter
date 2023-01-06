import pygame
import os
import sys
from random import random

pygame.display.set_caption("minehunter")

class Board():
    def __init__(self, size):
        self.size = size
        self.prob = 0.2
        self.lost = False
        self.numClicked = 0
        self.numNonBombs = 0
        self.temp = 0
        self.setBoard()
       


    def setBoard(self):
        self.board = []
        piecePos = 0
        for row in range (self.size[0]):
            rows = []
            for col in range(self.size[1]):
                hasBomb = random() < self.prob
                if (not hasBomb):
                    self.numNonBombs += 1
                piecePos += 1    
                piece = Piece(hasBomb, piecePos)
                rows.append(piece)
            self.board.append(rows)
        self.setNeighbors()

    def setNeighbors(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                piece = self.getPiece((row, col))
                neighbors = self.getListOfNeighbors((row, col))
                piece.setNeighbors(neighbors)
        

    def getListOfNeighbors(self, index):
        neighbors = []
        for row in range(index[0] - 1, index[0] + 2):
            for col in range(index[1] - 1, index[1] + 2):
                outOfBounds = row < 0 or row >= self.size[0] or col < 0 or col >= self.size[1]
                same = row == index[0] and col == index[1]
                if (same or outOfBounds):
                    continue
                neighbors.append(self.getPiece((row, col)))
        return neighbors

    def getSize(self):
        return self.size

    def getPiece(self, index):
        return self.board[index [0]][index [1]]

    def handleClick(self, piece, flag):
        if (piece.getClicked() or (not flag and piece.getFlagged())):
            return

        if (flag):
            piece.placeFlag()
            return

        piece.click()
        if (piece.getHasBomb()):
            self.lost = True
            return

        self.numClicked += 1

        if (piece.getNumAround() != 0):
            return
        # auskommentiert damit recursion aus ist
        # for neighbor in piece.getNeighbors():
        #     if (not neighbor.getHasBomb() and not neighbor.getClicked()):
        #         self.handleClick(neighbor, False)

    def getLost(self):
        return self.lost

    def getWin(self):
        return self.numNonBombs == self.numClicked


class Piece():
    def __init__(self, hasBomb, position):
        self.hasBomb = hasBomb
        self.clicked = False
        self.flagged = False
        self.position = position

    def getHasBomb(self):
        return self.hasBomb

    def getClicked(self):
        return self.clicked

    def getFlagged(self):
        return self.flagged

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
        self.setNumAround()

    def getNeighbors(self):
        return self.neighbors
    
    def setNumAround(self):
        self.numAround = 0
        for piece in self.neighbors:
            if (piece.getHasBomb()):
                self.numAround += 1
            else:
                pass

    def getNumAround(self):
        return self.numAround

    def placeFlag(self):
        self.flagged = not self.flagged

    def click(self):
        self.clicked = True
            

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
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    rightClick = pygame.mouse.get_pressed()[2]
                    self.handleClick(position, rightClick)
            self.draw()
            pygame.display.flip()
            if (self.board.getWin()):
                run = False
        pygame.quit()

    def draw(self):
        topLeft = (0, 0)
        for row in range(self.board.getSize()[0]):
            for col in range(self.board.getSize()[1]):
                piece = self.board.getPiece((row, col))
                image = self.getImage(piece)
                self.screen.blit(image, topLeft)
                topLeft = topLeft[0] + self.pieceSize[0], topLeft[1]
            topLeft = 0, topLeft[1] + self.pieceSize[1]

    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if (not fileName.endswith(".png")):
                continue
            image = pygame.image.load("images/" + fileName)
            image = pygame.transform.scale(image, self.pieceSize)
            self.images[fileName.split(".")[0]] = image

    def getImage(self, piece):
        string = None
        if (piece.getClicked()):
            string = "mine-clicked" if piece.getHasBomb() else str(piece.getNumAround())
        else:
            string = "flag" if piece.getFlagged() else "tile"
        return self.images[string]

    def handleClick(self, position, rightClick):
        # auskommentiert damit das Spiel nicht einfriert wenn man auf eine Mine drückt
        # if (self.board.getLost()):
        #     return
        index = position[1] // self.pieceSize[1], position[0] // self.pieceSize[0]
        piece = self.board.getPiece(index)
        self.board.handleClick(piece, rightClick)


size = (9, 9)
board = Board(size)
screenSize = (800, 800)
game = Game(board, screenSize)
game.run()

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

    pygame.display.update()