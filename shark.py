'''
1. At each chronon, the shark moves randomly to an adjacent square occupied
    by a fish. If there are none, the shark moves to a random adjacent unoccupied
    square. If there are no free squares, no movement takes place.
2. At each chronon, each shark is deprived of a unit of energy.
    Upon reaching zero energy, the shark dies.
3. If the shark moves to a square occupied by a fish, the shark eats the fish
    and earns a certain amount of energy.
4. Once the shark has survived a certain number of chronons it may reproduce in 
    exactly the same way as the fish.
'''

from creature import Creature
import random
import time

class Shark(Creature):
    'Predators of Wa-Tor'
    instances = []

    def __init__(self, x, y):
        self.energy = 8
        self.libido = 0
        self.x, self.y = x, y
        Shark.instances.append(self)

    def new_location(self, grid, new_column, new_row):
        if grid[new_column][new_row] == 0:
            grid[new_column][new_row] = 2
            if self.libido == 10:
                self.libido = 0
                shark = Shark(self.x, self.y)
            else:
                grid[self.x][self.y] = 0
            self.x, self.y = new_column, new_row
            return True
        else:
            return False

    def death(self, grid):
        grid[self.x][self.y] = 0
        Shark.instances.remove(self)
    