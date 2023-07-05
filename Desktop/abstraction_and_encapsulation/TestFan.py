#Importing class and modules
from Fan import Fan

# create two instances of the class Fan with diff parameters
my_fan1 = Fan(Fan.FAST, 10, 'yellow', True)
my_fan2 = Fan(Fan.MEDIUM,5,'blue',False)

# print the attributes of 2 fans
print("Fan 1 - Speed: {}, Radius: {}, Color: {}, Status: {}".format(my_fan1.get_speed(),my_fan1.get_radius(),my_fan1.get_color(),my_fan1.get_on()))

print("Fan 2 - Speed: {}, Radius: {}, Color: {}, Status: {}".format(my_fan2.get_speed(),my_fan2.get_radius(),my_fan2.get_color(),my_fan2.get_on()))