
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
CELLSIZE = 8
MARGIN = 2
WIDTH = 90
HEIGHT = 60
WINDOW_X = 900
WINDOW_Y = 600


class World:
    """The torus-shaped world of Wa-Tor."""
    
    def spawn_creature(self, grid, creature_type):
        """Randomly choose beginning location of creatures."""
        spawned = False
        while not spawned:
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

    def update_world(self, grid, screen):
        """At end of every chronon, redraw updated locations."""
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

    def create_world(self):
        """Initial setup for world grid."""
        grid = []
        for y in range(0, HEIGHT):
            grid.append([])
            for x in range(0, WIDTH):
                grid[y].append(0)
        return grid
        



def main(args):
    # Pygame initialize
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Population Dynamics | Wa-Tor")

    world = World()
    clock = pygame.time.Clock()
    chronons = args.num_chronons

    # World creation
    world_created = False
    while not world_created:
        screen.fill(BACKGROUND)
        new_world = world.create_world()
        for f in range(args.num_fish):
            world.spawn_creature(new_world, "fish")
        for s in range(args.num_sharks):
            world.spawn_creature(new_world, "shark")
        world_created = True

    # Main simulation loop
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
            world.update_world(new_world, screen)
            chronons -= 1

        pygame.display.flip()
        clock.tick(args.framerate)

    pygame.quit()
    sys.exit()


def parse_arguments():
    """Setup argument parser for user-edited simulation."""
    parser = argparse.ArgumentParser(description='Wa-Tor: Population Dynamics Simulation')
    parser.add_argument('-c', '--num_chronons', help='Runtime length. (Default: 1000)', default=1000, type=int)
    parser.add_argument('-f', '--num_fish', help='Number of fish. (Default: 120)', default=120, type=int)
    parser.add_argument('-s', '--num_sharks', help='Number of sharks. (Default: 40)', default=40, type=int)
    parser.add_argument('-fps', '--framerate', help='Framerate (Default: 20)', default=20, type=int)
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    main(parse_arguments())