
from creature import Creature
import random

class Fish(Creature):
    'Peaceful denizens of Wa-Tor'

    def __init__(self, x, y):
        self.energy = 1
        self.libido = 0
        self.x, self.y = x, y
        Creature.instances.append(self)

    def new_location(self, grid, new_column, new_row):
        if grid[new_column][new_row] == 0:
            grid[new_column][new_row] = 1
            if self.libido == 8:
                self.libido = 0
                fish = Fish(self.x, self.y)
            else:
                grid[self.x][self.y] = 0
            self.x, self.y = new_column, new_row
            return True
        else:
            return False

    def check_eaten(self, grid):
        if grid[self.x][self.y] == 2:
            print(self)
            Creature.instances.remove(self)
    