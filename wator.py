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

pygame.init()

# Color setup
BACKGROUND  = ( 52,  73,  94)
OCEAN       = ( 52, 152, 219)
FISH        = ( 46, 204, 113)
SHARK       = (230, 126,  34)
DEATH       = (231,  76,  60)
SPAWN       = (236, 240, 241)

# Window settings
screen_size = [800, 600]
screen = pygame.display.set_mode(screen_size)
block_width = 6
block_height = 6
block_margin = 1
pygame.display.set_caption("Population Dynamics | Wa-Tor")


class World:
    'The torus-shaped world of Wa-Tor'

    def __init__(self):
        self.lifespan = 100

    def spawnShark(self, grid):
        pos_x = random.randint(0, 79)
        pos_y = random.randint(0, 99)
        shark = Shark(pos_x, pos_y)
        grid[pos_x][pos_y] = 1
        print("(" + str(pos_y) + ", " + str(pos_x) + ")", Shark.count)

    def spawnFish(self, grid):
        pos_x = random.randint(0, 80)
        pos_y = random.randint(0, 100)
        fish = Fish(pos_x, pos_y)
        grid[pos_x][pos_y] = 1
        print("(" + str(pos_y) + ", " + str(pos_x) + ")", Fish.count)

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
    world = World()
    exit = False
    world_created = False
    clock = pygame.time.Clock()

    while not exit:
        while not world_created:
            screen.fill(BACKGROUND)
            created_world = world.createWorld()
            world_created = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Change screen coordinates to cartesian
                column, row = pos[0], pos[1]
                cart_coords = "(" + str(row) + ", " + str(column) + ")"
                print("Screen:", pos, "Grid: " + cart_coords)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    world.spawnShark(created_world)


        world.updateWorld(created_world)
        pygame.display.flip()
        clock.tick(5)

    pygame.quit()


if __name__ == "__main__":
    main()