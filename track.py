class Track:
    def __init__(self, x, y):
        self.x = x
        self.y = y
<<<<<<< HEAD
       
    def move(self, delt_x, delt_y):
        return Track(self.x + delt_x, self.y + delt_y)
   
    def distance(self, other_track):
        delt_x = self.x - other_track.x
        delt_y = self.y - other_track.y
       
        return (delt_x**2 + delt_y**2)**0.5
=======
        def move(self, delta_y, delta_x):
            return Track(self.x + delta_x, self.y + delta_y)
        def distance(self, other_track):
            delta_x = self.x - other_track.x
            delta_y = self.y - other_track.y
            return(delta_x**2 + delta_y**2)**0.5
>>>>>>> random
