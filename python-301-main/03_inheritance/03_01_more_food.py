# Create another child class that inherits from `Ingredient()`. You can use
# the code you wrote yourself, or continue working with the one provided below.
# Implement at least one extra method for your child class, and override the
# `expire()` method from the parent `Ingredient()` class.

class Ingredient:
    """Models an Ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient item."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __str__(self):
        return f"You have {self.amount} {self.name}."


class Spice(Ingredient): 
    """Models a spice to flavor your food."""

    def grind(self):
        print(f"You have now {self.amount} of ground {self.name}.")

    def chop(self):
        print(f"The spice {self.name} is now chopped ({self.amount}gr.)")

    def expire(self):
        print()
        if self.name == 'salt':
            print(f"{self.name} never expires. It has been in the sea for millions of years.")
        else:
            print(f"your {self.name} has expired. It's probably still good.")
            self.name = 'old ' + self.name

class Vegetable(Ingredient):
    def chop(self):
        print(f"Your {self.name} are now chopped in slices.")
    
    def expire(self):
        print(f"These {self.name} are not looking great.")


# p = Ingredient('peas', 12)
# print(p)
# s = Spice('salt', 200)
# print(s.expire())  # added expire method
# print()

# c = Ingredient('carrots', 3)
# p = Spice('pepper', 20)
# p.grind()  # ground pepper
# # c.grind()
# print()

# # chopped spices but not Ingredient()
# d = Spice('basil', 50)
# e = Ingredient('broccoli', 2)
# d.chop()
# # e.chop()
# print()

## Override a method
# f = Spice('salt', 10)
# f.expire()
# print(f)

## Create another child class Vegetable().
g = Vegetable('Beans', 15)
g.expire()
print(g)