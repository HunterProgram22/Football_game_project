# coding: utf-8
class team(object):
# Class with attribute of a team on a yardline
	def __init__(self, yardline = 20):
		self.yardline = yardline
		
	def yardchange(self, yardchange):
		self.yardline = self.yardline + yardchange
		
	def printyard(self):
		print(self.yardline)
		
class series(team):
# a series is an subclass of team to handle 4 downs to gain 10 yards
		def __init__(self, down = 1, yardstogo = 10):
			team.__init__(self)
			self.down = down
			self.yardstogo = yardstogo
			self.printdown()
			
		def printdown(self):
			print("It is %d down and %d yards to go on the %d yardline." % (self.down, self.yardstogo, self.yardline))
			print("-" * 30)
			
		def downchange(self, yards = 0):
			if yards >= self.yardstogo:
				self.down = 1
				self.yardstogo = 10
				self.yardchange(yards)
			else:
				if self.down >= 4:
					gameover()
				self.down = self.down + 1
				self.yardstogo = self.yardstogo - yards
				self.yardchange(yards)
			self.printdown()
		
		def getyardline(self):
			return self.yardline
			
def gameover():
	print("Turnover on downs. You lose!")
	exit(0)
