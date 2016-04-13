#Gamebler will play every turn for seven turns and never bow out before end of round 7. Boom or bust.
from Player_Class import Player
class GamblerPlayer(Player):

    def roll_again(self):
        return True
