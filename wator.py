
from creature import Creature
from fish import Fish
from shark import Shark
import random
import pygame
import argparse


# Color setup
BACKGROUND = ( 62,  70,  73)
OCEAN      = ( 47,  47,  49)
FISH       = ( 34, 168, 109)
SHARK      = (233, 110,  68)

# Window settings
pygame.init()
CELLSIZE = 10
MARGIN = 2
HEIGHT = 30
WIDTH = 30
screen_size = [500, 500]
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Population Dynamics | Wa-Tor")


class World:
    'The torus-shaped world of Wa-Tor'

    def spawnCreature(self, grid, creature_type):
        spawned = False
        while spawned == False:
            x = random.randint(0, HEIGHT - 1)
            y = random.randint(0, WIDTH - 1)
            if grid[x][y] == 0:
                spawned = True
        if creature_type == "fish":
            grid[x][y] = 1
            fish = Fish(x, y)
        elif creature_type == "shark":
            grid[x][y] = 2
            shark = Shark(x, y)

    def updateWorld(self, grid):
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                if grid[y][x] == 1:
                    color = FISH
                elif grid[y][x] == 2 or grid[y][x] == 3:
                    color = SHARK
                else:
                    color = OCEAN
                pygame.draw.rect(screen, color, 
                    [(MARGIN + CELLSIZE) * x + MARGIN, 
                    (MARGIN + CELLSIZE) * y + MARGIN, 
                    CELLSIZE, CELLSIZE])

    def createWorld(self):
        grid = []
        for y in range(0, HEIGHT):
            grid.append([])
            for x in range(0, WIDTH):
                grid[y].append(0)
        return grid
        



def main(args):

    world = World()
    clock = pygame.time.Clock()
    chronons = args.num_chronons

    world_created = False
    while not world_created:
        screen.fill(BACKGROUND)
        new_world = world.createWorld()
        for f in range(args.num_fish):
                world.spawnCreature(new_world, "fish")
        for s in range(args.num_sharks):
                world.spawnCreature(new_world, "shark")
        world_created = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                None

        if chronons > 0:
            for creature in Creature.instances:
                creature.check_status(new_world)
            world.updateWorld(new_world)
            chronons -= 1

        pygame.display.flip()
        clock.tick(args.framerate)

    pygame.quit()
    quit()

def parse_arguments():
    parser = argparse.ArgumentParser(description = "Wa-Tor: Population Dynamics Simulation")
    parser.add_argument('-c', '--num_chronons', help = "Runtime length. (Default: 100)", default = 100, type = int)
    parser.add_argument('-f', '--num_fish', help = "Number of fish. (Default: 6)", default = 6, type = int)
    parser.add_argument('-s', '--num_sharks', help = "Number of sharks. (Default: 2)", default = 2, type = int)
    parser.add_argument('-fps', '--framerate', help = "Framerate (Default: 8)", default = 8, type = int)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main(parse_arguments())