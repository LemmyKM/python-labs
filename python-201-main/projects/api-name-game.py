# Add an API call to your CLI game that assigns a name to your player.

import requests
import time
import sys


length_player_name = 0
while length_player_name < 2:
    player_name = input('Enter your name (between 2 and 40 characters long) : ')
    length_player_name = len(player_name)

URL = f"https://uzby.com/api.php?min={length_player_name}&max={length_player_name}"

uzby_name = requests.get(URL)

print(f"Hello {uzby_name.text}!  Welcome to the game.")
time.sleep(1)



# choice = None
# game = True
# sword = False

# # main loop
# while game:
#     choice = input("\nYou see two doors in front of you. Do you choose 'left' or 'right'? : ")
#     time.sleep(1)
#     print("Good luck!")
#     time.sleep(1)

#     # IN THE LEFT ROOM
#     if choice == 'left':
#         empty_room = input('\nYou entered an empty room. Would you like to exit(e) or have a (l)ook around? : ')
#         while True:
#             if empty_room == 'l':
#                 take_sword = input('\nLook at that! There is a sword hanging from the wall. Would you like to pick it up? (Answer "yes" or "no" : ')
#                 if take_sword == 'yes':
#                     sword = True
#                     print('\nGreat! This might come in handy later.')
#                     break
#                 elif take_sword == 'no':
#                     break
#                 break
#             elif empty_room == 'e':
#                 break
#     elif choice == 'right':
#         while True:
#             fight_or_flee = input("\nThere's a dragon in here!!! Do you want to fight it or flee? : ")
#             if fight_or_flee == 'flee':
#                 print('That sounds like a great plan. You need a weapon!')
#                 break
#             elif fight_or_flee == 'fight' and sword == True:
#                 print("\nThat's right! Kill the beast!! Well done! You won!")
#                 sys.exit()
#             elif fight_or_flee == 'fight':
#                 print("\nThat was a stupid decision! Without a weapon the dragon is tearing you to pieces!! You're dead!")
#                 sys.exit()
