# Use your `Ingredients` class to create a URL to an online search
# that allows to look for recipes for dishes made from the
# available ingredients.

import webbrowser
# import requests

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_info(self):
        self.name = self.name.title()  # --> search terms for wikipedia must be with a capital
        self.wiki = f"https://en.wikipedia.org/wiki/{self.name}"
#        response = requests.get(self.wiki)  no need for the requests module with 'webbrowser'
        webbrowser.open(self.wiki, new=2)

recipe = Ingredient('boeing', 11)
print(recipe.get_info())