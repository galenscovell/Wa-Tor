
from creature import Creature
import random

class Fish(Creature):
    'Peaceful denizens of Wa-Tor'
    instances = []

    def __init__(self, x, y):
        self.energy = 14
        self.libido = 0
        self.x, self.y = x, y
        Fish.instances.append(self)

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

    def death(self, grid):
        grid[self.x][self.y] = 0
        Fish.instances.remove(self)
    