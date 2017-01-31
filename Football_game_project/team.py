import players

class Team(object):
    'An object that has the team players as objects'
    def __init__(self, teamname='Lions'):
        self.teamname = teamname
        self.QB = players.QuarterBack()
        self.RB = players.RunningBack()
        self.WR = players.WideReceiver()
        self.team = [self.QB, self.RB, self.WR]
    
    def print_team(self):
        print(self.teamname)
        for players in self.team:
            print(players.name + '\t\t' + players.position)
            players.printstats()
            

