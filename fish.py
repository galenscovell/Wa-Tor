'''
1. At each chronon, the fish moves randomly to one of the adjacent unoccupied
    squares. If there are no free squares, no movement takes place.
2. Once the fish has survived a certain number of chronons it may reproduce. 
    This is done as it moves to a neighbouring square, leaving behind a new 
    fish in its old position. Its reproduction time is also reset to zero.
'''

from creature import *
import random

class Fish():
    'Peaceful denizens of Wa-Tor'
    count = 0
    instances = []

    def __init__(self, x, y):
        self.libido = random.randint(0, 3)
        Fish.count += 1
        self.x = x
        self.y = y
        Fish.instances.append(self)

    def movement(self, grid):
        row = self.y
        column = self.x
        moved = False
        options = [1, 2, 3, 4]
        while moved == False and len(options) > 0:
            pick = random.choice(options)

            if pick == 1:
                if (column+1) > 9:
                    options.remove(1)
                else:
                    if grid[column+1][row] == 0:
                        grid[column+1][row] = 2
                        grid[column][row] = 0
                        self.x = (column+1)
                        moved = True
                    else:
                        options.remove(1)


            elif pick == 2:
                if (column-1) < 0:
                    options.remove(2)
                else:
                    if grid[column-1][row] == 0:
                        grid[column-1][row] = 2
                        grid[column][row] = 0
                        self.x = (column-1)
                        moved = True
                    else:
                        options.remove(2)

            elif pick == 3:
                if (row+1) > 9:
                    options.remove(3)
                else:
                    if grid[column][row+1] == 0:
                        grid[column][row+1] = 2
                        grid[column][row] = 0
                        self.y = (row+1)
                        moved = True
                    else:
                        options.remove(3)

            elif pick == 4:
                if (row-1) < 0:
                    options.remove(4)
                else:
                    if grid[column][row-1] == 0:
                        grid[column][row-1] = 2
                        grid[column][row] = 0
                        self.y = (row-1)
                        moved = True
                    else:
                        options.remove(4)

