
from creature import Creature

class Fish(Creature):
    'Peaceful denizens of Wa-Tor'

    def __init__(self, x, y):
        self.handler = 1
        self.libido = 0
        self.x = x
        self.y = y
        Creature.instances.append(self)