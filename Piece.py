import pygame

class Piece (pygame.sprite.Sprite): 
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.highlight == False
	
	def highlighted(self):
		if (pygame.mouse.get_pressed == True and self.highlight == False):
			self.highlight == True
		elif(pygame.mouse.get_pressed == True and self.highlight == True):
			self.highlight == False

	def checkMove(self):
		#decide how you want this to happen mayhaps put it in the main
