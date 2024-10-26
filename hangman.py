# Hangman

import random
from hm import image

class Hangman(object):
	print('Welcome to Hangman.')
	print('Number of turns: 8')
	
	def beginning(self):
		while self.gamePlay == True:
			l.__init__()
			l.sowpods()
			l.choosing()
			l.game()
		
	def __init__(self):
		self.y = []
		self.blanks = []
		self.guessed = []
		self.repeat = []
		self.gamePlay = True
		self.turns = 8
		
	def sowpods(self):
		a = 'E:/Python/sowpods.txt'
		file = open(a, 'r')
		b = file.read()
		self.x = b.split('\n')

	def choosing(self):
		self.c = random.choice(self.x)
		
		if len(self.c) < 5:
			l.choosing()
			
		self.y = list(self.c)
		
#		print(self.y)

		b = self.x.index(self.c)
		self.x.remove(self.c)
		
		for i in self.y:
			self.blanks.append('_')
		
	def game(self):
	
		image(self)
		while self.turns > 0:
			for x in self.blanks:
				print(x, end = ' ')
				
			print('\nPreviously guessed letters are: ' + str(self.guessed))
				
			letter = input('Enter a letter: ')
			
			if letter.isalpha() == False:
				print('Please enter letters only.')
			elif letter.upper() in self.guessed:
				print('You have already guessed this letter.')
			elif len(letter.upper()) > 1:
				print('Please enter single letters only.')
			elif letter == '' or letter == ' ':
				print('You did not enter a letter.')
			elif (letter.upper() in self.y):
				for m in range(len(self.y)):
					if letter.upper() == self.y[m]:
						self.blanks[m] = letter.upper()
				print('Correct!')
			else:
				print('Incorrect letter.')
				self.turns -= 1
				
			if (letter.upper() in self.guessed) or len(letter) > 1 or letter == '' or letter == ' ' or letter.isalpha() == False:
				pass
			else:
				self.guessed.append(letter.upper())
				
			print('\nNumber of turns left: ' + str(self.turns))
			
			image(self) # From file 'hm.py'
				
			if self.turns == 0:
				for x in self.blanks:
					print(x, end = ' ')
					
				print('\n\nGame over. Correct letter was ' + self.c)
				break
					
			if self.y == self.blanks:
				for x in self.blanks:
					print(x, end = ' ')
					
				print('\nYou won the game!')
				break
			
		l.playAgain()

	def playAgain(self):
		ask = input('\nWould you like to play again(Y or N): ')
		if ask.upper() == 'Y':
			pass
		else:
			self.gamePlay = False
		print('\n--------------------------\n')

l = Hangman()
l.beginning()

# Hangman image is obtained from file 'hm.py'
# Method used in hm.py is easier to understand, another method might be to compile all elements of image into list.