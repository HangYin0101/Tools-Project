from utils import getRandomLocation
import random

class Snake:
    '''
    speed: speed of the snake. Default is 10, and can be adjusted for acceleration
    length: length of the snake. Default is 3, and will increase by 1 for each apple eaten
    num_apples: number of apples in map. (default:10)
    Grid_W, Grid_H: Grid_W and Grid_H must be provided when instantiating a Snake object
    '''
    
    def __init__(self, Grid_W, Grid_H, length=3, speed=10, num_apples = 10):
        
        self.x = random.randint(5, Grid_W - 6)
        self.y = random.randint(5, Grid_H - 6)
        
        # dictionary to store booleans on directions
        # makes it easy to handle directions, tail generation etc.
        self.direction_dict = {'left':0, "right":1,"up":0,"down":0}
        self.current_direction = 'right'
        
        self.length = length
        self.speed = speed
        self.apple_locations = [getRandomLocation(Grid_W, Grid_H) for i in range(self.num_apples)]
            
        self.coordinates = [{'x':self.x - i, 'y':self.y} for i in range(self.length)]
        
        # potentially useful but not necessary features
        self.alive = True
        self.lifetime = 0
    
    def next_move(self, self.
        
    
    def change_length(self, increment=1):
        self.length+=increment
        
        
                      
    def change_speed(self, speed_difference):
        if self.speed < speed_difference:
            print("speed cannot be changed to negative")
            return None
        else:
            self.speed += speed_difference
        
    def change_direction(self, direction):
        
        # one has to check if given direction is opposite, since the head location must then be changed
        # without changing the coordinates
        
        # change next direction in direction_dict to 1
        self.direction_dict[direction] = 1
        
        # if in the same direction, either left and right will both be 1, or up and down will both be 1
        if self.direction_dict['left'] * self.direction_dict['right'] == 1:
            self.direction_dict[direction] = 0

        # up down case
        elif self.direction_dict['up'] * self.direction_dict['down'] == 1:
            self.direction_dict[direction] = 0
        
        else:
            # change current direction in direction_dict to 0
            self.direction_dict[self.current_direction] = 0

            # change current_direction
            self.current_direction = direction
    
    def kill(self): 
        self.alive = False
 