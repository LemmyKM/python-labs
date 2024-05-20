# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():

    def __init__(self, name):
        self.name = name

    def distance_sun(self):
        if self.name == 'Mercury':
            return "Average distance from Mercury to the sun is 57 million km."
        elif self.name == 'Venus':
            return "Average distance from Venus to the sun is 108 million km." 
        elif self.name == 'Earth':
            return "Average distance from Earth to the sun is 150 million km."
        elif self.name == 'Mars':
            return "Average distance from Mars to the sun is 228 million km."
        elif self.name == 'Jupiter':
            return "Average distance from Jupiter to the sun is 779 million km."
        elif self.name == 'Saturn':
            return "Average distance from Saturn to the sun is 1.43 billion km."
        elif self.name == 'Uranus':
            return "Average distance from Uranus to the sun is 2.88 billion km."
        elif self.name == 'Neptune':
            return "Average distance from Neptune to the sun is 4.50 billion km."

    def temperature(self):
        if self.name == 'Mercury':
            return "Temperature of Mercury is from -173 to 426.7 degrees C." 
        elif self.name == 'Venus':
            return "Temperature of Venus is on average 482 degrees C." 
        elif self.name == 'Earth':
            return "Temperature on Earth is on average 19 degrees C."
        elif self.name == 'Mars':
            return "Temperature on Mars is from -113 to 0 degrees C."
        elif self.name == 'Jupiter':
            return "Temperature on Jupiter is on average -145 degrees C."
        elif self.name == 'Saturn':
            return "Temperature on Saturn is on average -178 degrees C."
        elif self.name == 'Uranus':
            return "Temperature on Uranus is on average -195 degrees C."
        elif self.name == 'Neptune':
            return "Temperature on Neptune is on average -193 degrees C."


planet_ = Planet('Mercury')
print(planet_.distance_sun())

planet_ = Planet('Saturn')
print(planet_.temperature())