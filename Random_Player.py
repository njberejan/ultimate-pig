#Random_Player has a 50% chance of quitting after every round.
class Random(Player):

    def __init__(self, personality):
        self.personality = personality
