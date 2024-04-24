# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def house(**kwargs):
    print(f"Property description : ")
    for k, v in kwargs.items():
        print(f" * {k} {v}")
    
house(Area=': Fourways', address=': 38 Bommerskonten', oppm2=': 234', zwembad=': yes', garage=': 2 cars')
