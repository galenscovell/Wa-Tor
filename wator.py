'''
1. Wa-Tor is usually implemented as a 2-dimensional grid with 3 colours, 
    one for fish, one for sharks and one for empty water. 
2. If a creature moves past the edge of the grid, it reappears on the 
    opposite side. The sharks are predatory and eat the fish. 
'''

from shark import *
from fish import *
import random
import pygame


# Color setup
BACKGROUND  = ( 62,  70,  73)
OCEAN       = ( 47,  47,  49)
FISH        = ( 34, 168, 109)
SHARK       = (233, 110,  68)
DEATH       = (231,  76,  60)
SPAWN       = (240, 240, 240)

# Window settings
pygame.init()
screen_size = [800, 500]
screen = pygame.display.set_mode(screen_size)
block_width = 30
block_height = 30
block_margin = 6
pygame.display.set_caption("Population Dynamics | Wa-Tor")


class World:
    'The torus-shaped world of Wa-Tor'

    def __init__(self, lifespan, s_pop, f_pop):
        self.lifespan = lifespan
        self.shark_population = s_pop
        self.fish_population = f_pop


    def spawnCreature(self, grid, creature_type):
        spawned = False
        while spawned == False:
            pos_x = random.randint(0, 9)
            pos_y = random.randint(0, 9)
            if grid[pos_x][pos_y] == 0:
                spawned = True
        if creature_type == "shark":
            grid[pos_x][pos_y] = 1
            shark = Shark(pos_x, pos_y)
        else:
            grid[pos_x][pos_y] = 2
            fish = Fish(pos_x, pos_y)


    def updateWorld(self, grid):
        for row in range(10):
            for column in range(10):
                if grid[row][column] == 1:
                    color = SHARK
                elif grid[row][column] == 2:
                    color = FISH
                else:
                    color = OCEAN
                pygame.draw.rect(screen, color, [(block_margin + block_width) * column + block_margin, (block_margin + block_height) * row + block_margin, block_width, block_height])


    def createWorld(self):
        grid = []
        for row in range(10):
            grid.append([])
            for column in range(10):
                grid[row].append(0)
        return grid
        



def main():

    # World creation variables (chronons, sharks, fish)
    world = World(200, 3, 6)

    world_created = False
    clock = pygame.time.Clock()
    chronons = world.lifespan

    while chronons > 0:
        while not world_created:
            screen.fill(BACKGROUND)
            created_world = world.createWorld()
            for s in range(world.shark_population):
                    world.spawnCreature(created_world, "shark")
            for f in range(world.fish_population):
                    world.spawnCreature(created_world, "fish")
            world_created = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Change screen coordinates to cartesian
                column, row = pos[0], pos[1]
                cart_coords = "(" + str(row) + ", " + str(column) + ")"
                print("Screen:", pos, "Grid: " + cart_coords)


        for fish in Fish.instances:
            fish.movement(created_world)
        world.updateWorld(created_world)
        pygame.display.flip()
        clock.tick(10)
        chronons -= 1


if __name__ == "__main__":
    main()