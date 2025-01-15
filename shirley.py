import random

class PowerUp:
    def __init__(self, chance=0.2):
        self.chance = chance 

    def activate(self, base_damage):
        if random.random() < self.chance:
            return base_damage * 2
        else:
            return base_damage