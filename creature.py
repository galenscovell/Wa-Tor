
import random
HEIGHT = 40
WIDTH = 60

class Creature():
    """Base class for all creatures of Wa-tor."""
    instances = []

    def check_adjacent_cells(self, grid):
        """
        Create dictionary of all adjacent cells contents, 
        adjusting for horizontal wrap-around.
        Cells outside of vertical height are thrown out.
        Dictionary contents are either 0 (empty), 1 (fish) or 2 (shark).
        """
        results = {}
        for x, y in [(self.x + i, self.y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if i != 0 or j != 0]:
                if (0 <= x < HEIGHT):
                    # Allow wrap-around on horizontal axis
                    if y == WIDTH:
                        y = 0
                    elif y < 0:
                        y = WIDTH - 1
                    results[x,y] = grid[x][y]
        return results

    def movement(self, grid):
        """
        Using results from check_adjacent_cells, 
        have creaturesrespond to environment.
        Sharks do not move to other shark spaces. 
        If there are nearby fish, shark randomly selects one to pursue. 
        Sharks gain energy and libido when they eat a fish.
        Fish randomly choose move based on adjacent free spaces.
        If there are no empty adjacent spaces, no movement occurs.
        If creature libido >= 12, new creature of same type is 
        spawned in their old space.
        """
        moved = False
        open_spaces = self.check_adjacent_cells(grid)

        # Shark behavior
        if self.handler == 2:
            nearby_fish = [k for k,v in open_spaces.items() if v == 1]
            if len(nearby_fish) > 0:
                move_options = nearby_fish
                self.energy += 1
                self.libido += 1
            else:
                move_options = [k for k,v in open_spaces.items() if v == 0]

        # Fish behavior
        elif self.handler == 1:
            move_options = [k for k,v in open_spaces.items() if v == 0]

        if len(move_options) == 0:
            moved = True
        while not moved:
            choice = random.randint(0, len(move_options) - 1)
            new_x = move_options[choice][0]
            new_y = move_options[choice][1]
            if self.libido >= 12:
                self.libido = 0
                grid[self.x][self.y] = self.handler
                self.__module__ = type(self)(self.x, self.y)
            else:
                grid[self.x][self.y] = 0
            self.x = new_x
            self.y = new_y
            grid[new_x][new_y] = self.handler
            moved = True

    def check_status(self, grid):
        """Check energy at beginning of chronon for death event."""
        # Check each shark status
        if self.__class__.__name__ == 'Shark':
            if self.energy <= 0:
                grid[self.x][self.y] = 0
                Creature.instances.remove(self)
            else:
                self.energy -= 1
                self.movement(grid)

        # Check each fish status
        elif self.__class__.__name__ == 'Fish':
            if grid[self.x][self.y] == 2:
                Creature.instances.remove(self)
            else:
                self.libido += 3
                self.movement(grid)


