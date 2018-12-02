import random

class Snake:
    '''
    speed: speed of the snake. Default is 10, and can be adjusted for acceleration
    length: length of the snake. Default is 3, and will increase by 1 for each apple eaten
    num_apples: number of apples in map. (default:10)
    Grid_W, Grid_H: Grid_W and Grid_H must be provided when instantiating a Snake object
    '''
    
    def __init__(self, Grid_W, Grid_H, length=3, speed=5):
        
        self.x = random.randint(5, Grid_W - 6)
        self.y = random.randint(5, Grid_H - 6)
        
        # dictionary to store booleans on directions
        # makes it easy to handle directions, tail generation etc.
        self.direction_dict = {'left':0, "right":1,"up":0,"down":0}
        self.current_direction = 'right'
        
        self.length = length
        self.speed = speed
        
        self.coordinates = [{'x':self.x - i, 'y':self.y} for i in range(self.length)]
        
        self.alive = True
        self.eating= False
        self.Grid_W = Grid_W
        self.Grid_H = Grid_H
    
    def move_to_next_position(self):
        
        # add head coordinates
        new_position = {'x':self.x + self.direction_dict['right'] - self.direction_dict['left'], 
                        'y': self.y - self.direction_dict['up'] + self.direction_dict['down']}
        
        # check if new position is already in coordinates
        if new_position in self.coordinates[:-1]:
            self.kill()
        
        # check if new position is outside window, which should kill
        elif self.check_if_outside_window(new_position['x'],new_position['y']):
            self.kill()
        
        # if not then next move doesn't kill snake
        else:
            
            self.coordinates.insert(0,new_position)
            
            # remove tail coordinates
            if self.eating==False:
                self.coordinates = self.coordinates[:-1]
            else:
                self.eating = False
            
            self.x = new_position['x']
            self.y = new_position['y']
            
    # helper function for checking whether next move is in window        
    def check_if_outside_window(self,x,y):
        if (x*y < 0) | (x == self.Grid_W) | (y == self.Grid_H):
            return True
        return False
            
    def change_length(self, increment=1):
        self.length+=increment

                      
    def change_speed(self, speed_difference=5):
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
            if direction != self.current_direction:
                self.direction_dict[self.current_direction] = 0

            # change current_direction
            self.current_direction = direction
    
    def kill(self): 
        self.alive = False
        
    def set_eating(self):
        self.eating = True

def getRandomLocation(Grid_W=40, Grid_H=25):
    return {'x': random.randint(0, Grid_W - 1), 'y': random.randint(0, Grid_H - 1)}
 