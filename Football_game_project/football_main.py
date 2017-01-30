# coding: utf-8
import firstdown 
import playbook

			
def game():
	team = input("Enter a team name: ")
	drive = firstdown.series()
	while drive.getyardline() <= 100:
		yardgain = playbook.play()
		print("You selected a " + yardgain.playchoice + 
			" play and the defense selected a " + yardgain.defense +
			 " play. \n") 
		if yardgain.playgain() < 0:
			print("The loss on that play is %d yards. \n" % yardgain.playgain())
		elif yardgain.playgain() == 0:
			print("There is no gain on that play.")
		else:
			print("The gain on that play is %d yards. \n" % yardgain.playgain())
		drive.downchange(yardgain.playgain())
	print("Touchdown the %s win!" % team)
	

		
										
game()
		
