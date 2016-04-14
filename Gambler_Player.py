#Gamebler will play every turn for seven turns and never bow out before end of round 7. Boom or bust.
from Player_Class import Player
class GamblerPlayer(Player):
    #__innit__ IS NOT NEEDED BECAUSE ATTRIBUTES DEFINED IN PARENT CLASS WON'T CHANGE FOR CHILD CLASSES
    def roll_again(self):
        return True
