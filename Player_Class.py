# The Rules of Pig Solitaire
# In 7 turns, you are attempting to get the highest score possible.
#
# Each turn, you have two choices:
#
# Roll. Roll a six-sided die. If it comes up one, your turn is over and you add nothing to your score. If it comes up two through six, you add that number to your turn total and choose again.
# Hold. If you hold, you add the turn total to your score.
# An example:
#
# The first turn, I roll a 1 immediately. I receive no points.
#
# The second turn, I roll a 5. I choose to roll again. I roll a 3, for a turn total of 8. I choose to roll again. I roll a 3, for a turn total of 11. I hold, receiving 11 points. My score is 11.
#
# The third turn, I roll a 5 again. I choose to roll again. I roll a 6, for a turn total of 11. I choose to roll again. I roll a 4, for a turn total of 15. I decide to roll once more. I roll a 6, for a turn total of 21. I hold, receiving 21 points. My score is 32.
#
# The fourth turn, I roll a 6. I choose to roll again. I roll a 3, for a turn total of 9. I choose to roll again. I roll a 3, for a turn total of 12. I choose to roll again. I roll a 4, for a turn total of 16. I hold, receiving 16 points. My score is 48.
#
# The fifth turn, I roll a 6. I choose to roll again. I roll a 6, for a turn total of 12. I choose to roll again. I roll a 3, for a turn total of 15. I choose to roll again. I roll a 4, for a turn total of 19. I choose to roll again. I roll a 6, for a turn total of 25. I hold, receiving 25 points. My score is 73.
#
# The sixth turn, I roll a 6. I choose to roll again. I roll a 1, and receive no points.
#
# The seventh turn, I roll a 5. I choose to roll again. I roll a 1, and receive no points.
#
# My final score is 73.

import math
import random
from Random_Player import RandomPlayer
from Gambler_Player import GamblerPlayer
# import statistics as st
# import numpy as np
# import matplotlib.pyplot as plt

class Player:

    def __init__(self, personality):
        self.personality = personality #my idea being that the personality aspect determines how they play game below
        self.game_score = 0
        self.turn = 0

    def roll_a_die(self):
        return random.randint(1, 6)

    def roll_again(self):
        return False

# DID NUMBER OF TURNS WRONG. EACH SERIES IS ONE "TURN"

    # def turn_decision(self):
    #     if self.personality

    def turn(self):
        roll_results_list = []
        while True:
            roll = self.roll_a_die()
            if roll == 1:
                roll_results_list = [0]
                # print('You rolled a one, end of turn. You rolled {} times.'.format(roll_number))
                return sum(roll_results_list)
            else:
                roll_results_list.append(roll)
                roll_or_hold = self.roll_again()
                if roll_or_hold == False:
                    # print('You choose not to roll. Your score is {} in {} turns'.format(sum(roll_results_list), roll_number))
                    return sum(roll_results_list)
                else:
                    roll_number += 1
                    roll_results_list.append(roll)
                    continue
        # print('The game is over. Your score is {} in {} turns.'.format(sum(roll_results_list), roll_number))
        self.game_score.append(roll_results_list)
        return sum(roll_results_list)

    def game(self):
        while self.turn < 7:
            turn()

trial_results = []
for _ in range(20):
    player = Random('basic')
    game()
    trial_results.append(player.turn())
print(trial_results)
