#Random_Player has a 50% chance of quitting after every round.
from Player_Class import Player
class RandomPlayer(Player):
    #__innit__ IS NOT NEEDED BECAUSE ATTRIBUTES DEFINED IN PARENT CLASS WON'T CHANGE FOR CHILD CLASSES
    def roll_again(self):
        return random.choice([True, False])
