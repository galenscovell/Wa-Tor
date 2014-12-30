'''
1. At each chronon, the fish moves randomly to one of the adjacent unoccupied
    squares. If there are no free squares, no movement takes place.
2. Once the fish has survived a certain number of chronons it may reproduce. 
    This is done as it moves to a neighbouring square, leaving behind a new 
    fish in its old position. Its reproduction time is also reset to zero.
'''

from creature import *
import random

class Fish(Creature):
    'Peaceful denizens of Wa-Tor'
    count = 0
    instances = []

    def __init__(self, x, y):
        self.libido = 0
        Fish.count += 1
        self.x = x
        self.y = y
        Fish.instances.append(self)

    def check_status(self, grid):
        if grid[self.x][self.y] == 1:
            grid[self.x][self.y] = 0
            Fish.instances.remove(self)
            print("Fish death!")
        elif self.libido >= 3:
            self.libido = 0

    def new_location(self, grid, column_change, row_change):
        new_column = self.x + column_change
        new_row = self.y + row_change
        if grid[new_column][new_row] == 0:
            grid[new_column][new_row] = 1
            grid[self.x][self.y] = 0
            self.x = new_column
            self.y = new_row
            return True
        else:
            return False