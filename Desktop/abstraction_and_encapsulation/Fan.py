# Create a class Fan
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def init(self, speed=SLOW, radius=5, color='blue', on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on
    # get and set methods for class Fan
    def get_speed(self):
        return self.speed
    def set_speed(self)
        return self.speed 