# importing class and modules
from Car import Car
# create object for a class Car
my_car = Car(2022, 'BMW')

#accelerate the car five times
for i in range(5):
    my_car.accelerate()
    print("car accelerating current speed:" , my_car.get_speed())
#brake the car five times
for i in range(5):
    my_car.brake()
    print("current speed when the car is braking:" , my_car.get_speed())