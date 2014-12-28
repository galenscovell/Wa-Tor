'''
1. At each chronon, the shark moves randomly to an adjacent square occupied
    by a fish. If there are none, the shark moves to a random adjacent unoccupied
    square. If there are no free squares, no movement takes place.
2. At each chronon, each shark is deprived of a unit of energy.
    Upon reaching zero energy, the shark dies.
3. If the shark moves to a square occupied by a fish, the shark eats the fish
    and earns a certain amount of energy.
4. Once the shark has survived a certain number of chronons it may reproduce in 
    exactly the same way as the fish.
'''

class Shark:
    def __init__(self, name):
        self.name = name
        self.energy = 10
        self.libido = 4