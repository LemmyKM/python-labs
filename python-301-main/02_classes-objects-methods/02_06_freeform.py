# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

from time import sleep

class Dishwasher:
    def __init__(self, cutlery, glasses, mugs, plates):
        self.cutlery = cutlery
        self.glasses = glasses
        self.mugs = mugs
        self.plates = plates

    def __str__(self):
       return f"The content of the dishwasher is {self.cutlery} pieces of cutlery, {self.glasses} glasses, {self.mugs} mugs and {self.plates} plates."

    def start(self):
        return 'the dishwasher is on and has started ...'
        # time.sleep(6)
        # print('Dishes are clean!')

dishes = Dishwasher(17, 12, 11, 16)
print(dishes)
cycle = dishes.start()
print(cycle)


class Bike:
    def __init__(self, brakes, tyres, speed):
        self.brakes = brakes
        self.tyres = tyres
        self.speed = speed

    def __str__(self):
        return f"Your bike's brakes are {self.brakes}, the tyres are {self.tyres} and you're going at {self.speed} km/h."

        

wheels = Bike('faulty', 'flat', 60)
print(wheels)



class Laptop:
    def __init__(self, power, temperature, screen):
        self.power = power
        self.temperature = temperature
        self.screen = screen

    def __str__(self):
        pass
    
