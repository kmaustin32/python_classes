from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:

    print(' rock... \n paper... \n scissors... \n')
    options = ['rock', 'paper', 'scissors']

    p1_input = input('Player 1\'s choice > ').lower()
    p2_input = options[randint(0, 2)]

    if p1_input == 'quit' or p1_input == 'q':
        quit()

    if (p1_input == 'rock' or p1_input == 'paper' or p1_input == 'scissors') and (p2_input == 'rock' or p2_input == 'paper' or p2_input == 'scissors'):

        print(f'Player 2\'s choice > {p2_input}')

        if p1_input == p2_input:
            print('Oh no, it\'s a tie!')
        else:
            if p1_input == 'rock' and p2_input == 'scissors':
                player_wins += 1
                print('Player 1 wins!')
            elif p1_input == 'paper' and p2_input == 'rock':
                player_wins += 1
                print('Player 1 wins!')
            elif p1_input == 'scissors' and p2_input == 'paper':
                player_wins += 1
                print('Player 1 wins!')
            else:
                print('Player 2 wins!')
                computer_wins += 1

        print(f'player score: {player_wins}; computer score: {computer_wins}')

    else:
        print("Sorry, one of you entered an invalid option.")

if player_wins > computer_wins:
    print('Player wins best 2 of 3!')
else:
    print('Computer wins best 2 of 3!')