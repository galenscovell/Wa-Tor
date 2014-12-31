
import random
HEIGHT = 20
WIDTH = 20

class Creature():
    'Base class for all creatures of Wa-tor'
    instances = []

    def check_adjacent_cells(self, grid):
        results = {}
        for x, y in [(self.x + i, self.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
                if (0 <= x <= WIDTH - 1) and (0 <= y <= HEIGHT - 1):
                    results[x,y] = grid[x][y]
        return results

    def movement(self, grid):
        open_spaces = self.check_adjacent_cells(grid)
        possible_spots = [k for k,v in open_spaces.items() if v == 0]
        choice = random.randint(0, len(possible_spots) - 1)
        new_x = possible_spots[choice][0]
        new_y = possible_spots[choice][1]
        if self.libido == 8:
            grid[self.x][self.y] = self.handler
            self.__module__ = type(self)(self.x, self.y)
        else:
            grid[self.x][self.y] = 0
        self.x = new_x
        self.y = new_y
        grid[new_x][new_y] = self.handler

    def check_status(self, grid):
        if self.__class__.__name__ == 'Shark':
            if self.energy == 0:
                grid[self.x][self.y] = 0
                Creature.instances.remove(self)
            else:
                self.energy -= 1
                self.libido += 0.5
                self.movement(grid)
        elif self.__class__.__name__ == 'Fish':
            self.fish_checks()
            self.movement(grid)


