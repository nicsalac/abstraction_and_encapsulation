# Create a class Fan
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on
    # get and set methods for class Fan
    def get_speed(self):
        return self.speed
    def set_speed(self,speed):
        self.speed = speed
    def get_on(self):
        return self.on
    def set_on(self,on):
        self.on = on
    def get_radius(self):
        return self.radius
    def set_radius(self,radius):
        self.radius = radius
    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color = color

