import random
 
class  wandering:
    def __init__(self, name):
        self.name = name
       
class ComunWandering(wandering):
    def __init__(self, name):
        super().__init__(name)
<<<<<<< HEAD
       
    def walk(self):
        return random.choice([(0,2),(0,-2),(2,0),(-2,0)])
=======
    def walk(self):
        return random.choice([(0,3)(0,-3)(3,0)(-3,0)])
>>>>>>> random
