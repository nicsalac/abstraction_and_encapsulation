# Importing class and modules
from Fan import Fan

my_fan1 = Fan(Fan.FAST, 10, 'yellow', True)
# my_fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)

# print the attributes of 2 fans
print("Fan 1 - Speed:", my_fan1.get_speed(), "Radius:", my_fan1.get_radius(), "Color:", my_fan1.get_color(), "Status:", my_fan1.get_on())

my_fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)
print("Fan 2 - Speed:", my_fan2.get_speed(), "Radius:", my_fan2.get_radius(), "Color:", my_fan2.get_color(), "Status:", my_fan2.get_on())  # corrected the print statements and added ',' between attributes
