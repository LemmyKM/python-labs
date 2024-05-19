class Dog:
    species = 'Canis familiaris'    # class attribute

    def __init__(self, name, age):  # Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.
        self.name = name   # instance attribute
        self.age = age   # instance attribute

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

