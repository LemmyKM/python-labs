# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

import random

class Pokemon:
    def __init__(self, name, primary_type, hp, max_hp):
        self.name = input('What is your name? : ').capitalize()
        self.primary_type = ['water', 'fire', 'grass']
        self.hp = 4
        self.max_hp = 10

    def battle(self):
        while True:
            print(f"Fight now {self.name}!")
            user_power = input('Enter 0 for Water, 1 for Fire, 2 for grass')