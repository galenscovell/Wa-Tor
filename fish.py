'''
1. At each chronon, the fish moves randomly to one of the adjacent unoccupied
    squares. If there are no free squares, no movement takes place.
2. Once the fish has survived a certain number of chronons it may reproduce. 
    This is done as it moves to a neighbouring square, leaving behind a new 
    fish in its old position. Its reproduction time is also reset to zero.
'''

from creature import *

class Fish(Creature):
    'Peaceful denizens of Wa-Tor'
    count = 0

    def __init__(self, x, y):
        self.libido = 3
        Fish.count += 1
        Creature.plus(self)