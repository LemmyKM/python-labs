import webbrowser

class Soup:
    def __init__(self) -> None:
        self.name = input('Which soup are you making? : ')
        self.amount_people = int(input("For how many people? : "))
        self.ingredients = 'soup' + ' ' + self.name + ' ' + input("Which ingredients would you like to use? : ")
    
    def spice(self, *args):
        return f"I am adding the following spices : {args}."
    
    def cook(self):
        self.recipe = f"https://www.allrecipes.com/search?q={self.ingredients}"
        webbrowser.open(self.recipe, new=2)

potage = Soup()
potage.cook()