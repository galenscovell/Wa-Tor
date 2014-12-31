
from creature import Creature
import random

class Shark(Creature):
    'Predators of Wa-Tor'

    def __init__(self, x, y):
        self.energy = 10
        self.libido = 0
        self.x, self.y = x, y
        Creature.instances.append(self)

    def new_location(self, grid, new_column, new_row):
        if grid[new_column][new_row] == 2:
            return False
        else:
            if grid[new_column][new_row] == 1: 
                self.energy += 4
            #if self.libido == 10:
                #self.libido = 0
                #shark = Shark(self.x, self.y)
            grid[self.x][self.y] = 0
            grid[new_column][new_row] = 2
            self.x, self.y = new_column, new_row
            return True

    def death(self, grid):
        grid[self.x][self.y] = 0
        Creature.instances.remove(self)
    