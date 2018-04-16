import pygame
#create a method in main to ensure that no more than one piece is highlighted 
#add in a check if jumped feature somewhere else
class Board:
    def __init__ ( self, screen ):
            self.board = list()
            self.blackCheckers = list()
            self.redCheckers = list()
            self.clearList = list()
            self.refreshList = list()

            blackRow = list()
            redRow = list()

    self.screen = screen
    for i in range ( 4 ):
            blackRow.append ( ( 128, 0, 0 ) )
            blackRow.append ( ( 10, 10, 10 ) )
            redRow.append ( ( 10, 10, 10 ) )
            redRow.append ( ( 128, 0, 0 ) )

    for i in range ( 4 ):
		self.board.append ( blackRow )
		self.board.append ( redRow )

   def drawBoard ( self ):
		x = 0
		y = 0

    for row in self.board:
        for square in row:
                pygame.draw.rect ( self.screen, square, ( x * 50, y * 50, 50, 50 ), 0 )
                x += 1
                x = 0
                y += 1

    pygame.display.flip()

   def drawCheckers ( self ):
        for address in self.blackCheckers:
                refreshRect = pygame.draw.circle ( self.screen, ( 0, 0, 0 ), ( address [ 0 ] * 50 + 25, address [ 1 ] * 50 + 25 ), 20, 0 )
                self.refreshList.append ( refreshRect )
        for address in self.redCheckers:
		refreshRect = pygame.draw.circle ( self.screen, ( 200, 0, 0 ), ( address [ 0 ] * 50 + 25, address [ 1 ] * 50 + 25 ), 20, 0 )
		self.refreshList.append ( refreshRect )

   def clearSpace ( self ):
        for address in self.clearList:
                refreshRect = pygame.draw.rect ( self.screen, self.board [ address [ 0 ] ] [ address [ 1 ] ], ( address [ 0 ] * 50, address [ 1 ] * 50, 50, 50 ), 0 )
                self.refreshList.append ( refreshRect )

   def update ( self ):
        self.clearSpace()
        self.drawCheckers()
        pygame.display.update ( self.refreshList )
        self.refreshList = list()

pygame.display.init()
screen = pygame.display.set_mode ( ( 640, 480 ) )

game = checkers ( screen )

game.drawBoard()
game.redCheckers.append ( ( 3, 0 ) )
game.blackCheckers.append ( ( 4, 2 ) )
game.clearList.append ( ( 3, 0 ) )
game.clearList.append ( ( 5, 0 ) )
game.update()

raw_input()
pygame.quit()


class Piece extends sprite: 
	def __init__(self):
		self.highlight == False
	
	def highlighted(self):
		if (pygame.mouse.get_pressed == True and self.highlight == False):
			self.highlight == True
		elif(pygame.mouse.get_pressed == True and self.highlight == True):
			self.highlight == False

	def checkMove(self):
		#decide how you want this to happen mayhaps put it in the main

	
#sprite = pygame.image.load('#blahblah.png')