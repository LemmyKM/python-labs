# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

import time
import sys

player_name = input('\nEnter your name : ')
time.sleep(1)
print()
print(f"Hello {player_name}!  Welcome to the game.")
time.sleep(1)

choice = None
game = True
sword = False

# main loop
while game:
    choice = input("\nYou see two doors in front of you. Do you choose 'left' or 'right'? : ")
    time.sleep(1)
    print("Good luck!")
    time.sleep(1)

    # IN THE LEFT ROOM
    if choice == 'left':
        empty_room = input('\nYou entered an empty room. Would you like to exit(e) or have a (l)ook around? : ')
        while True:
            if empty_room == 'l':
                take_sword = input('\nLook at that! There is a sword hanging from the wall. Would you like to pick it up? (Answer "yes" or "no" : ')
                if take_sword == 'yes':
                    sword = True
                    print('\nGreat! This might come in handy later.')
                    break
                elif take_sword == 'no':
                    break
                break
            elif empty_room == 'e':
                break
    elif choice == 'right':
        while True:
            fight_or_flee = input("\nThere's a dragon in here!!! Do you want to fight it or flee? : ")
            if fight_or_flee == 'flee':
                print('That sounds like a great plan. You need a weapon!')
                break
            elif fight_or_flee == 'fight' and sword == True:
                print("\nThat's right! Kill the beast!! Well done! You won!")
                sys.exit()
            elif fight_or_flee == 'fight':
                print("\nThat was maybe not a great decision! Without a weapon the dragon is tearing you to pieces!! You're dead!")
                sys.exit()


