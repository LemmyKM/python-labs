import random
import time

class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        print(f"Our knight {self.name} attacks {opponent.name}")

        hero_dice = random.randint(1, 20)
        opp_dice = random.randint(1, 20)

        print("Our knight raises powerfield ...")
        time.sleep(3)
        print(f"{hero_dice}...")
        print(f"{opponent.name} raises powerfield ...")
        time.sleep(3)
        print(f"{opp_dice}...")
        time.sleep(2)

        if hero_dice >= opp_dice:
            print("Our knight prevails and lives to see another day!")
        else:
            print(f"{opponent.name} is the stronger warrior today!")

class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack():
        pass


class Weak_Opponent:
    pass

def start_game():
    opponents = [
        Opponent('Belzebub', 20),
        Opponent('Pilatus', 10),
        Opponent('Herodes', 5),
        Opponent('Matteus', 7),
        Opponent('Lucas', 15),
    ]
    hero = Hero('Jesus', 20)

    while True:
        current_opponent = random.choice(opponents)
        print()
        print(f"The gates of Hell are opened and {current_opponent.name} with a power level of {current_opponent.level} materialises in front of {hero.name}.")
        act = input("Do you want to [s]trike, (f)lee or (l)ook around? ")
        print()
        while act not in ['s', 'f', 'l', 'q']:
            print('please enter [s, f, l]')
            print('To quit the game enter [q]')
            act = input("Do you want to [s]trike, (f)lee or (l)ook around? ")

        if act == 's':
            if hero.attack(current_opponent):
                opponents.remove(current_opponent)
            else:
                None
        elif act == 'f':
            print(f"These sandals are not suited to take on {current_opponent.name}. I will fight him another day when I am wearing my allstars.")
        
        elif act == 'l':
            print(f"{hero.name} sees the light, and also sees {current_opponent.name} with power level {current_opponent.level}")

        elif act == 'q':
            print('See you again on Easter day...')
            break


start_game()