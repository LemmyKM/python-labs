# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread_type, *toppings):
    sentence = f"This sandwich contains : {bread_type} bread, "
    for topping in toppings:
        sentence += topping + ', '
    print(sentence)
    

make_sandwich('brown', 'kaas', 'ajuin', 'mayo', 'basilicum')
