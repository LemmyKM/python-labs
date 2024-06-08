# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Aircraft:
    def __init__(self, type, engines_nr, engine_type):
        self.type = type
        self.engines_nr = engines_nr
        self.engine_type = engine_type

class Boeing(Aircraft):
    def __init__(self, type, engines_nr, engine_type, seats):
        super().__init__(type, engines_nr, engine_type)
        self.seats = seats

class Helicopter(Boeing):
    def __init__(self, type, engines_nr, engine_type, wheels_skid):
        super().__init__(type, engines_nr, engine_type)
        self.wheels_skid = wheels_skid

class Cessna:
    def __init__(self, type, wing, wheels):
        self.type = type
        self.wing = wing
        self.wheels = wheels

    def __str__(self):
        return f"The Cessna {self.type} has a {self.wing} wing and {self.wheels} wheels."

b = Boeing(747, 4, 'turbine', 267)
print(b.seats, b.type)

c = Cessna(210, 'high', 'retractable')
print(c)

d = Cessna(190, 'high', 'fixed')
print(d)