'''
1. At each chronon, the fish moves randomly to one of the adjacent unoccupied
    squares. If there are no free squares, no movement takes place.
2. Once the fish has survived a certain number of chronons it may reproduce. 
    This is done as it moves to a neighbouring square, leaving behind a new 
    fish in its old position. Its reproduction time is also reset to zero.
'''

class Fish:
    'Peaceful denizens of Wa-Tor'
    count = 0

    def __init__(self):
        self.libido = 3
        Fish.count += 1

    #def reproduce(self):
        # Reproduction

    #def move(self):
        # Behavior