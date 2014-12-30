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

from creature import *
import random

class Shark(Creature):
    'Predators of Wa-Tor'
    count = 0
    instances = []

    def __init__(self, x, y):
        self.energy = random.randint(4, 10)
        self.libido = 0
        Shark.count += 1
        self.x = x
        self.y = y
        Shark.instances.append(self)

    def check_status(self, grid):
        if grid[self.x][self.y] == 3:
            grid[self.x][self.y] = 2
            self.energy += 3

        #if self.energy <= 0:
            #grid[self.x][self.y] = 0
            #Shark.instances.remove(self)

        elif self.libido >= 6:
            self.libido = 0

    def new_location(self, grid, column_change, row_change):
        new_column = self.x + column_change
        new_row = self.y + row_change
        if grid[new_column][new_row] == 0:
            grid[new_column][new_row] = 2
            grid[self.x][self.y] = 0
            self.x = new_column
            self.y = new_row
            return True
        else:
            return False

    #def check_prey(self, grid):
    