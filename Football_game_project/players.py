class Player(object):
    'Common base class for all players'
    
    def __init__(self, name=None):
        self.name = name
        
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
        
    def printstats(self):
        self.updatestats()
        for stat in self.stats:
            print(stat[0] + '\t\t' + str(stat[1]))
 
 
        
class QuarterBack(Player):
    def __init__(self, name=None):
        Player.__init__(self)
        self.name = name
        self.passatt = 0
        self.passcomp = 0
        self.passyds = 0
        self.runatt = 0
        self.runyds= 0
        
                      
    def updatestats(self):
        self.stats = [('Pass Attempts', self.passatt), 
                      ('Pass Comp', self.passcomp), 
                      ('Pass Yards', self.passyds), 
                      ('Run Attempts', self.runatt), 
                      ('Run Yards', self.runyds)
                      ]