'''
1. Wa-Tor is usually implemented as a 2-dimensional grid with 3 colours, 
    one for fish, one for sharks and one for empty water. 
2. If a creature moves past the edge of the grid, it reappears on the 
    opposite side. The sharks are predatory and eat the fish. 
'''

from fish import Fish
from shark import Shark
import random
import pygame


# Color setup
BACKGROUND = ( 62,  70,  73)
OCEAN      = ( 47,  47,  49)
FISH       = ( 34, 168, 109)
SHARK      = (233, 110,  68)
DEATH      = (231,  76,  60)
SPAWN      = (240, 240, 240)

# Window settings
pygame.init()
screen_size = [500, 500]
screen = pygame.display.set_mode(screen_size)
block_width = 20
block_height = 20
block_margin = 6
pygame.display.set_caption("Population Dynamics | Wa-Tor")


class World:
    'The torus-shaped world of Wa-Tor'

    def __init__(self, lifespan, f_pop, s_pop):
        self.lifespan = lifespan
        self.fish_population = f_pop
        self.shark_population = s_pop

    def spawnCreature(self, grid, creature_type):
        spawned = False
        while spawned == False:
            pos_x = random.randint(0, 9)
            pos_y = random.randint(0, 9)
            spawn_pos = grid[pos_x][pos_y]
            if spawn_pos == 0:
                spawned = True
        if creature_type == "fish":
            spawn_pos = 1
            fish = Fish(pos_x, pos_y)
        else:
            spawn_pos = 2
            shark = Shark(pos_x, pos_y)

    def updateWorld(self, grid):
        for row in range(10):
            for column in range(10):
                if grid[row][column] == 1:
                    color = FISH
                elif grid[row][column] == 2:
                    color = SHARK
                else:
                    color = OCEAN
                pygame.draw.rect(screen, color, 
                    [(block_margin + block_width) * column + block_margin, 
                    (block_margin + block_height) * row + block_margin, 
                    block_width, block_height])

    def createWorld(self):
        grid = []
        for row in range(10):
            grid.append([])
            for column in range(10):
                grid[row].append(0)
        return grid
        



def main():

    # World creation variables (chronons, fish, sharks)
    world = World(200, 1, 2)
    clock = pygame.time.Clock()
    chronons = world.lifespan

    # World and creature creation
    world_created = False
    while not world_created:
        screen.fill(BACKGROUND)
        new_world = world.createWorld()
        for f in range(world.fish_population):
                world.spawnCreature(new_world, "fish")
        for s in range(world.shark_population):
                world.spawnCreature(new_world, "shark")
        world_created = True

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                None

        # Simulation loop
        while chronons > 0:
            for fish in Fish.instances:
                fish.movement(new_world)
                fish.libido += 1
                fish.energy -= 1
            for shark in Shark.instances:
                shark.movement(new_world)
                shark.libido += 1
                shark.energy -= 1
            world.updateWorld(new_world)
            pygame.display.flip()
            clock.tick(8)
            chronons -= 1

        clock.tick(30)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()