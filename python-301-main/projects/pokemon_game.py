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
import sys

class Pokemon:
    def __init__(self) -> None:
        self.name = input('What is your name? : ').capitalize()
        self.primary_type = ['water', 'fire', 'grass']
        self.hp = 4
        self.max_hp = 10

    def battle(self):
        # water > fire > grass > water
        while True:
            print(f"Fight now {self.name}!")
            user_choice = input('Enter 0 for Water, 1 for Fire, 2 for Grass.\n3 to feed more HP.\n4 to "Quit". : ').lower()
            print()
            battle_choice = [0, 1, 2]
            computer_choice = random.choice(battle_choice)
            if user_choice == '4':
                sys.exit()
            elif user_choice == '3':
                self.feed()
            elif user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice < computer_choice and user_choice < 2:
                    if self.hp == self.max_hp:
                        print(f'You won. Computer choice is {self.primary_type[computer_choice].title()}.')
                        print('You reached Max HP.')
                    else:
                        self.hp += 1
                        print(f'You won. Computer choice is {self.primary_type[computer_choice].title()}.')
                        print(f"Your HP is {self.hp}.")
                elif user_choice > computer_choice and user_choice < 3:
                    self.hp -= 1
                    print(f"You lost. Computer choice is {self.primary_type[computer_choice].title()}.")
                    print(f"Your HP is {self.hp}.")
                    if self.hp == 0:
                        print('Game Over.')
                        break
                elif user_choice == computer_choice:
                    print("It's a draw.")
                    print(f'Your HP is {self.hp}.')
                else:
                    print('That is not an option. Try again.')
            else:
                print('That is not an option. Try again.')

    def feed(self):
        if self.hp <= 5:
            self.hp += 3
            print(f"You gained 3 HP. Current HP is {self.hp}.")
        elif self.hp > 5:
            self.hp += 1
            print(f"You gained 1 HP. Current HP is {self.hp}.")
        else:
            print(f"You can't feed for the moment. You already have Max HP {self.max_hp}.")

p = Pokemon()
p.battle()