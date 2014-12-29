'''
1. Wa-Tor is usually implemented as a 2-dimensional grid with 3 colours, 
    one for fish, one for sharks and one for empty water. 
2. If a creature moves past the edge of the grid, it reappears on the 
    opposite side. The sharks are predatory and eat the fish. 
'''

from shark import *
from fish import *
from creature import *
import random
import pygame


# Color setup
BACKGROUND  = ( 52,  73,  94)
OCEAN       = ( 52, 152, 219)
FISH        = ( 46, 204, 113)
SHARK       = (230, 126,  34)
DEATH       = (231,  76,  60)
SPAWN       = (236, 240, 241)

# Window settings
pygame.init()
screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)
block_width = 6
block_height = 6
block_margin = 1
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
            pos_x = random.randint(0, 79)
            pos_y = random.randint(0, 99)
            if grid[pos_x][pos_y] == 0:
                spawned = True
        if creature_type == "shark":
            grid[pos_x][pos_y] = 1
            shark = Shark(pos_x, pos_y)
        else:
            grid[pos_x][pos_y] = 2
            fish = Fish(pos_x, pos_y)
        print(Creature.count, Shark.count, Fish.count)


    def updateWorld(self, grid):
        for row in range(80):
            for column in range(100):
                if grid[row][column] == 1:
                    color = SHARK
                elif grid[row][column] == 2:
                    color = FISH
                else:
                    color = OCEAN
                pygame.draw.rect(screen, color, [(block_margin + block_width) * column + block_margin, (block_margin + block_height) * row + block_margin, block_width, block_height])


    def createWorld(self):
        grid = []
        for row in range(80):
            grid.append([])
            for column in range(100):
                grid[row].append(0)
        return grid
        



def main():

    # World creation variables (chronons, sharks, fish)
    world = World(100, 100, 200)

    loop = True
    world_created = False
    clock = pygame.time.Clock()

    while loop:
        while not world_created:
            screen.fill(BACKGROUND)
            created_world = world.createWorld()
            world_created = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for s in range(world.shark_population):
                        world.spawnCreature(created_world, "shark")
                    for f in range(world.fish_population):
                        world.spawnCreature(created_world, "fish")


        world.updateWorld(created_world)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()