import numpy as np
class twodice: 
    ''' 
    Creating an object that will roll two 6-sided dice 
    '''

    #First we need a constructor 
    #Attributes of the class 
    def __init__(self, d1 = None, d2 = None):
        ''' 
        Arguments:
        d1: sets the dice face of die 1 
        d2: similar to d1 
        If d1 (d2) = None, the user is allowing the dice face to be randomly chosen 
        '''
        if d1 is None: 
            self.x = np.random.randint(1,7)
        else: 
            self.x = d1
        if d2 is None: 
            self.y = np.random.randint(1,7)
        else: 
            self.y = d2
    #Methods of the class
    # ALL methods of a class must have the fisrt argument self 
    def roll(self):
        ''' 
        No arguments required
        Function to roll the dice 
        '''
        self.x = np.random.randint(1,7)
        self.y = np.random.randint(1,7)
        
    def is_success(self, target):
        ''' 
        Checking if the ice rolled greater than or equal to a target number 
        Arguments: 
        target: value user is hoping to meet or exceed
        '''
        return self.x + self.y >= target 

