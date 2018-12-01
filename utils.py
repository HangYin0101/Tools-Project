import random

def getRandomLocation(Grid_W, Grid_H):
    return {'x': random.randint(0, Grid_W - 1), 'y': random.randint(0, Grid_H - 1)}
