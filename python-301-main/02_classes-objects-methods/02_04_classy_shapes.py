# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def circumference(self):
        return 2 * 3.14 * self.radius



rectangle = Rectangle(3, 4)
print(f"The area for the rectangle is {rectangle.area()}cm2.")
print(f"The perimeter for the rectangle is {rectangle.perimeter()}cm.")
print()

circle = Circle(4)
print(f"The area for the circle is {circle.area()}cm2.")
print(f"The circumference for the circle is {circle.circumference()}cm.")