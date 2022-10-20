# this file will be used to create the game logic for our RPSLS game
# we will need to import the classes from the player and gestures folders
from player.human import Human
from player.computer import Computer
# we will need to import the sleep method from the time module to add a delay to the game
from time import sleep
# we will need to create a method that will display a greeting to the user
def display_greeting():
    print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    sleep(1)
    print('\nThe rules are simple: ')
    sleep(1)
    print('Scissors cuts Paper')
    sleep(1)
    print('Paper covers Rock')
    sleep(1)
    print('Rock crushes Lizard')
    sleep(1)
    print('Lizard poisons Spock')
    sleep(1)
    print('Spock smashes Scissors')
    sleep(1)
    print('Scissors decapitates Lizard')
    sleep(1)
    print('Lizard eats Paper')
    sleep(1)
    print('Paper disproves Spock')
    sleep(1)
    print('Spock vaporizes Rock')
    sleep(2)
    print('And as it always has, Rock crushes Scissors')
# we will need to create a method that will ask the user which game mode they would like to play
def create_game_mode():
    print('\nPlease choose a game mode: ')
    sleep(1)
    print('1. Single Player')
    print('2. Multiplayer')
    print('3. Demo Mode')
    sleep(1)
    mode = int(input('\nPlease enter the number of your choice: '))
    if mode == 1:
        return 'computer'
    elif mode == 2:
        return 'human'
    elif mode == 3:
        return 'demo'
    else:
        print('Invalid choice. Please try again.')
        create_game_mode()
    return mode
# we will need to create a method that will ask the user how many wins are needed to win the game
def create_win_goal() -> int:
    wins = int(input('\nPlease enter the number of wins needed to win the game: '))
    if wins == 3 or wins == 5 or wins == 7:
        return wins
    else:
        print('Invalid choice.\nPlease choose either 3, 5, or 7\nPlease try again.')
        create_win_goal()
    return wins
# this method will be used to create the players for the game based on the game mode given from the create_game_mode method
def create_players(mode):
    if mode == 'computer':
        return [Human(), Computer()]
    elif mode == 'human':
        return [Human(), Human()]
    elif mode == 'demo':
        return [Computer(), Computer()]
# this method will be used to compare the gestures of the players
def compare_gestures(players):
    player1 = players[0]
    player2 = players[1]
    if player1.choice.name == player2.choice.name:
        print('\nIt\'s a tie! No points awarded.')
    elif player1.choice.name == 'rock':
        if player2.choice.name == 'scissors' or player2.choice.name == 'lizard':
            print(f'\n{player1.name} wins this round!')
            player1.score += 1
        else:
            print(f'\n{player2.name} wins this round!')
            player2.score += 1
    elif player1.choice.name == 'paper':
        if player2.choice.name == 'rock' or player2.choice.name == 'spock':
            print(f'\n{player1.name} wins this round!')
            player1.score += 1
        else:
            print(f'\n{player2.name} wins this round!')
            player2.score += 1
    elif player1.choice.name == 'scissors':
        if player2.choice.name == 'paper' or player2.choice.name == 'lizard':
            print(f'\n{player1.name} wins this round!')
            player1.score += 1
        else:
            print(f'\n{player2.name} wins this round!')
            player2.score += 1
    elif player1.choice.name == 'lizard':
        if player2.choice.name == 'paper' or player2.choice.name == 'spock':
            print(f'\n{player1.name} wins this round!')
            player1.score += 1
        else:
            print(f'\n{player2.name} wins this round!')
            player2.score += 1
    elif player1.choice.name == 'spock':
        if player2.choice.name == 'rock' or player2.choice.name == 'scissors':
            print(f'\n{player1.name} wins this round!')
            player1.score += 1
        else:
            print(f'\n{player2.name} wins this round!')
            player2.score += 1
    sleep(2)
    print(f'\n{player1.name} has {player1.score} points.')
    sleep(1)
    print(f'{player2.name} has {player2.score} points.')
# this method will be used to display the winner and the final score
def display_final_score(players):
    player1 = players[0]
    player2 = players[1]
    if player1.score > player2.score:
        print(f'\n{player1.name} wins the game!')
    elif player2.score > player1.score:
        print(f'\n{player2.name} wins the game!')
    else:
        print('\nThe game is a tie!')
    print(f'\n{player1.name} has {player1.score} points.')
    print(f'{player2.name} has {player2.score} points.')
# this method will be used to ask the user if they would like to play again
def play_again():
    print('\nWould you like to play again?')
    sleep(1)
    print('1. Yes')
    print('2. No')
    sleep(1)
    choice = int(input('\nPlease enter the number of your choice: '))
    if choice == 1:
        print('\nStarting a new game...')
        return True
    elif choice == 2:
        print('\nThank you for playing!')
        return False
    else:
        print('Invalid choice. Please try again.')
        play_again()
    return choice