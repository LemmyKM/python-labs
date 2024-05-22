# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.


class Car:
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase_speed(self):
        inc_speed = self.max_speed + 5
        return inc_speed
    
    def doors(self):
        return "number of doors = 4"
    
    def color(self):
        return 'Color is yellow with blue dots.'
    
    def __str__(self):
        return f"Car model : {self.model}\nYear of construction : {self.year}\nMax speed : {self.max_speed}\n"
print()
car = Car('Toyota Prius', 2015, 160)
print(car)

print(car.increase_speed())
print(car.doors())
print(car.color())