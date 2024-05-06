# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.

sheep = input('enter a name for the sheep : ')

if len(sheep) > 4:
    print(f"{sheep} has a lot of wool.")
else:
    print(f"{sheep} is likely to produce more wool if you allocate him a longer name. Try again.")
