
from creature import Creature
from fish import Fish
from shark import Shark
import pygame, random, argparse, sys


# Color setup
BACKGROUND = ( 62,  70,  73)
OCEAN      = ( 47,  47,  49)
FISH       = ( 34, 168, 109)
SHARK      = (233, 110,  68)

# Constant setup
CELLSIZE = 9
MARGIN = 1
HEIGHT = 50
WIDTH = 50
WINDOW_X = 500
WINDOW_Y = 500


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

    def updateWorld(self, grid, screen):
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                if grid[y][x] == 1:
                    color = FISH
                elif grid[y][x] == 2:
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

    # Pygame initial setup
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Population Dynamics | Wa-Tor")

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
            world.updateWorld(new_world, screen)
            chronons -= 1

        pygame.display.flip()
        clock.tick(args.framerate)

    pygame.quit()
    sys.exit()

def parse_arguments():
    parser = argparse.ArgumentParser(description = "Wa-Tor: Population Dynamics Simulation")
    parser.add_argument('-c', '--num_chronons', help = "Runtime length. (Default: 1000)", default = 1000, type = int)
    parser.add_argument('-f', '--num_fish', help = "Number of fish. (Default: 80)", default = 80, type = int)
    parser.add_argument('-s', '--num_sharks', help = "Number of sharks. (Default: 20)", default = 20, type = int)
    parser.add_argument('-fps', '--framerate', help = "Framerate (Default: 10)", default = 10, type = int)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main(parse_arguments())