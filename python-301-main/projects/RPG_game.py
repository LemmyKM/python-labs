import random
from time import sleep
class Hero:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, opponent):
        print(f"Our knight {self.name} attacks {opponent.name}")

        hero_dice = random.randint(1, 20)
        opp_dice = random.randint(1, 20)

        print("Our knight raises powerfield ...")
        sleep(3)
        print(f"{hero_dice}...")
        print(f"{opponent.name} raises powerfield ...")
        sleep(3)
        print(f"{opp_dice}...")

        if hero_dice >= opp_dice:
            print("Our knight prevails and lives to see another day!")
        else:
            print(f"{opponent.name} is the stronger warrior today!")

class Opponent:
    def __init__(self, name, level):
        self.name = name
        self.level = level


a = Hero('Gabriel', 10)
print(a.attack)