
import random

class Creature():
    'Base class for all creatures of Wa-tor'

    def within_bounds(self, grid, column_change, row_change):
        new_column = self.x + column_change
        new_row = self.y + row_change
        if (0 <= new_column <= 9) and (0 <= new_row <= 9):
            self.new_location(grid, new_column, new_row)
            return True
        else:
            return False

    def movement(self, grid):
        if self.energy == 0:
            self.death(grid)
        else:
            moved = False
            options = [1, 2, 3, 4]
            while moved == False and len(options) > 1:
                pick = random.choice(options)
                if pick == 1:
                    if self.within_bounds(grid, 1, 0):
                        moved = True
                    else:
                        options.remove(1)
                elif pick == 2:
                    if self.within_bounds(grid, -1, 0):
                        moved = True
                        return True
                    else:
                        options.remove(2)
                elif pick == 3:
                    if self.within_bounds(grid, 0, 1):
                        moved = True
                        return True
                    else:
                        options.remove(3)
                elif pick == 4:
                    if self.within_bounds(grid, 0, -1):
                        moved = True
                        return True
                    else:
                        options.remove(4)
