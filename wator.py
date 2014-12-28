'''
1. Wa-Tor is usually implemented as a 2-dimensional grid with 3 colours, 
    one for fish, one for sharks and one for empty water. 
2. If a creature moves past the edge of the grid, it reappears on the 
    opposite side. The sharks are predatory and eat the fish. 
'''

from shark import *
from fish import *

class World():
    def __init__(self):
        self.lifespan = 100
        

def main():
    shark1 = Shark("sharkfriend")
    print(shark1.name, shark1.libido)
    fish1 = Fish("fishfriend")
    print(fish1.name, fish1.libido)


'''
If the python interpreter is running a module (the source file) as the main 
program, it sets the special __name__ variable to have a value "__main__". 
If this file is being imported from another module, __name__ will be set to 
the module's name.
'''
if __name__ == "__main__":
    main()