#Random_Player has a 50% chance of quitting after every round.
from Player_Class import Player
class RandomPlayer(Player):

    def roll_again(self):
        return random.choice([True, False])
