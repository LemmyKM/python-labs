"""Rock, Paper, Scissors"""

import sys, random, time

wins = 0
losses = 0
ties = 0

while True: # main loop
    while True: # keep asking until player enters R, P, S or Q
        print(f"{wins} Wins, {losses} Losses, {ties} Ties.")
        print("Enter your move : (R)ock, (P)aper, (S)cissors or (Q)uit.")
        player_move = input("> ").upper()
        if player_move == 'Q':
            print('Thanks for playing.')
            sys.exit()
        if player_move == 'R' or player_move == 'P' or player_move == 'S':
            break
        else:
            print('Please enter one of "R", "P", "S" or "Q".')
    
    # Display player choice :
    if player_move == 'R':
        print('ROCK versus ...')
        player_move = 'ROCK'
    elif player_move == 'P':
        print('PAPER versus ...')
        player_move = 'PAPER'
    elif player_move == 'S':
        print('SCISSORS versus ...')
    
    # three step delay :
    print('3...')
    time.sleep(0.5)
    print('2...')
    time.sleep(0.5)
    print('1...')
    time.sleep(0.5)
    print()

    # computer choice :
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_move = 'ROCK'
    elif random_number == 2:
        computer_move = 'PAPER'
    elif random_number == 3:
        computer_move = 'SCISSORS'
    print(computer_move)
    time.sleep(0.5)
    print()

    # display wins/losses/ties :
    if player_move == computer_move:
        print("It's a tie!")
        ties += 1
    elif player_move == 'ROCK' and computer_move == 'PAPER':
        print('You lose!')
        losses += 1
    elif player_move == 'ROCK' and computer_move == 'SCISSORS':
        print('You win!')
        wins += 1
    elif player_move == 'PAPER' and computer_move == 'ROCK':
        print('You win!')
        wins += 1
    elif player_move == 'PAPER' and computer_move == 'SCISSORS':
        print('You loose!')
        losses += 1
    elif player_move == 'SCISSORS' and computer_move == 'ROCK':
        print('You loose!')
        losses += 1
    elif player_move == 'SCISSORS' and computer_move == 'PAPER':
        print('You win!')
        wins += 1

