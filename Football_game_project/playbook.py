# coding: utf-8
import random

defplay = ['run', 'pass']

class play(object):
	# A play is a single object that will return a distance
	def __init__(self):
		self.defense = random.choice(defplay)
		self.playchoice = input("Choose a run or pass play.\n")
		if 'un' in self.playchoice:
			self.runplay()
		elif 'ass' in self.playchoice:
			self.passplay()
			
	def runplay(self):
		self.run = input("Run a QB sneak, a HB sweep, or FB dive. \n")
		if 'neak' in self.run:
			if self.defense == 'run':
				self.gain = random.randint(-2, 0)
			else:
				self.gain = random.randint(0, 2)
		elif 'weep' in self.run:
			if self.defense == 'run':
				self.gain = random.randint(-4, 5)
			else:
				self.gain = random.randint(0, 10)
		elif 'ive' in self.run:
			if self.defense == 'run':
				self.gain = random.randint(-2, 2)
			else: 
				self.gain = random.randint(1, 6)
	
	def passplay(self):
		self.pass_play = input("Run a screen pass, a fly pass, or deep pass \n")
		if 'reen' in self.pass_play:
			if self.defense == 'pass':
				self.gain = random.randint(-2, 1)
			else:
				self.gain = random.randint(-1, 8)
		elif 'ly' in self.pass_play:
			if self.defense == 'pass':
				self.gain = random.randint(-2, 6)
			else:
				self.gain = random.randint(0, 12)
		elif 'eep' in self.pass_play:
			if self.defense == 'pass':
				self.gain = random.randint(-5, 0)
			else: 
				self.gain = random.randint(10, 25)
		
	
	def playgain(self):
		return self.gain
