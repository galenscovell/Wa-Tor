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

BLACK   = (   0,   0,   0)
GREEN   = (   0, 255,   0)
BLUE    = (   0,   0, 255)

# Window settings
size = [800, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Population Dynamics | Wa-Tor")


class World:
    'The torus-shaped world of Wa-Tor'

    def __init__(self, name):
        self.name = name
        self.lifespan = 100


    def drawWorld(self, grid):
        height = 5
        width = 5
        margin = 2
        for row in range(80):
            for column in range(100):
                color = BLUE
                pygame.draw.rect(screen, color, [(margin + width) * column + margin, (margin + height) * row + margin, width, height])

    def createWorld(self):
        grid = []
        for row in range(80):
            grid.append([])
            for column in range(100):
                grid[row].append(0)
        return grid
        


def main():
    world1 = World("Test World")
    shark1 = Shark("Sharkfriend")
    fish1 = Fish("Fishfriend")

    shark1.showStats()
    fish1.showStats()
    print(fish1.symbol + ": " + str(Fish.count))
    print(shark1.symbol + ": " + str(Shark.count))

    print(World.__doc__ + ", " + World.__module__)
    print(Shark.__doc__ + ", " + Shark.__module__)
    print(Fish.__doc__ + ", " + Fish.__module__)

    

    exit = False
    world_created = False
    clock = pygame.time.Clock()

    # Main
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Change screen coordinates to cartesian
                column, row = pos[0], pos[1]
                cart_coords = "(" + str(row) + ", " + str(column) + ")"
                print("Screen:", pos, "Grid: " + cart_coords)

        screen.fill(BLACK)
        while not world_created:
            created_world = world1.createWorld()
            world_created = True

        world1.drawWorld(created_world)
        pygame.display.flip() # Update screen
        clock.tick(5)

    pygame.quit()

if __name__ == "__main__":
    main()