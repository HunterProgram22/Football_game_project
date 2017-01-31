class Player(object):
    'Common base class for all players'
    
    def __init__(self, name=None, position=None):
        self.name = name
        self.position = position
        self.passatt = 0
        self.passcomp = 0
        self.passyds = 0
        self.runatt = 0
        self.runyds= 0
        self.receptions = 0
        self.recyds = 0
        
        
    def runplay(self, yards):
        self.runyds = yards
        self.runatt += 1
        
    def passplay(self, passcomplete, yards=0):
        if passcomplete:
            self.passatt += 1
            self.passcomp += 1
            self.passyds = yards
        else:
            self.passatt += 1
            
    def passcatch(self, yards):
        self.recyds = yards
        self.receptions += 1
        
    def printstats(self):
        self.updatestats()
        print('-' * 30)
        print(self.name + '\t\t' + self.position)
        for stat in self.stats:
            print(stat[0] + '\t\t' + str(stat[1]))
        print('-' * 30)
 
 
        
class QuarterBack(Player):
    def __init__(self, name='Tyler', position='Quarterback'):
        Player.__init__(self)
        self.name = name
        self.position = position
      
                     
    def updatestats(self):
        self.stats = [('Pass Attempts', self.passatt), 
                      ('Pass Comp', self.passcomp), 
                      ('Pass Yards', self.passyds), 
                      ('Run Attempts', self.runatt), 
                      ('Run Yards', self.runyds)
                      ]
        

class RunningBack(Player):
    def __init__(self, name='Hunter', position='Runningback'):
        Player.__init__(self)
        self.name = name
        self.position = position

        
    def updatestats(self):
        self.stats = [('Run Attempts', self.runatt), 
                      ('Run Yards', self.runyds),
                      ('Receptions', self.receptions),
                      ('Receiving Yds', self.recyds)
                      ]


class WideReceiver(Player):
    def __init__(self, name='Zoe', position='Widereceiver'):
        Player.__init__(self)
        self.name = name
        self.position = position

        
    def updatestats(self):
        self.stats = [('Receptions', self.receptions),
                      ('Receiving Yds', self.recyds),
                      ('Run Attempts', self.runatt), 
                      ('Run Yards', self.runyds),   
                      ]









