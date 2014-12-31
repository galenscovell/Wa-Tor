
import random
HEIGHT = 30
WIDTH = 30

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
        moved = False
        open_spaces = self.check_adjacent_cells(grid)
        if self.handler == 2:
            nearby_fish = [k for k,v in open_spaces.items() if v == 1]
            if len(nearby_fish) > 0:
                move_options = nearby_fish
                self.energy += 4
            else:
                move_options = [k for k,v in open_spaces.items() if v == 0]
        elif self.handler == 1:
            move_options = [k for k,v in open_spaces.items() if v == 0]

        if len(move_options) == 0:
            moved = True
        while not moved:
            choice = random.randint(0, len(move_options) - 1)
            new_x = move_options[choice][0]
            new_y = move_options[choice][1]
            if self.libido == 10:
                grid[self.x][self.y] = self.handler
                self.__module__ = type(self)(self.x, self.y)
            else:
                grid[self.x][self.y] = 0
            self.x = new_x
            self.y = new_y
            grid[new_x][new_y] = self.handler
            moved = True

    def check_status(self, grid):
        if self.__class__.__name__ == 'Shark':
            if self.energy == 0:
                grid[self.x][self.y] = 0
                Creature.instances.remove(self)
            else:
                self.energy -= 1
                self.libido += 1
                self.movement(grid)
        elif self.__class__.__name__ == 'Fish':
            if grid[self.x][self.y] == 2:
                Creature.instances.remove(self)
            else:
                self.libido += 2
                self.movement(grid)


