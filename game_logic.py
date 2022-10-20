from player.human import Human
from player.computer import Computer
from gestures.creategesturelist import create_gestures
from gestures.rock import Rock
from gestures.paper import Paper
from gestures.scissors import Scissors
from gestures.lizard import Lizard
from gestures.spock import Spock
from time import sleep
# we will create a class that will hold the game logic
class Game:
    def __init__(self):
        self.gestures = create_gestures()
        self.players = []
        self.wins = 0
# it will have a method that will display the greeting
    def display_greeting(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        sleep(1)
# it will have a method that will display the rules
    def display_rules(self):
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
# it will have a method that will create the game mode
    def create_game_mode(self):
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
            self.create_game_mode()
        return mode
# it will have a method that will create the win goal
    def create_win_goal(self):
        num_wins = int(input('\nPlease enter the number of wins needed to win the game: '))
        if num_wins == 3 or num_wins == 5:
            return num_wins
        else:
            print('Invalid choice.\nPlease choose either 3 or 5\nPlease try again.')
            self.create_win_goal()
# it will have a method that will create the players
    def create_players(self, mode):
        if mode == 'computer':
            self.players.append(Human())
            print(f'\n{self.players[0].name} is ready to play!')
            self.players.append(Computer())
            print(f'{self.players[1].name} is ready to play!')
        elif mode == 'human':
            self.players.append(Human())
            print(f'\n{self.players[0].name} is ready to play!')
            self.players.append(Human())
            print(f'{self.players[1].name} is ready to play!')
        elif mode == 'demo':
            self.players.append(Computer())
            print(f'\n{self.players[0].name} is ready to play!')
            self.players.append(Computer())
            print(f'{self.players[1].name} is ready to play!')
        return self.players
# it will have a method that will compare the gestures given by the players
    def compare_gestures(self, player1, player2):
        # if the players choose the same gesture, it will be a tie and no one will get a point
        if player1.gesture.name == player2.gesture.name:
            print(f'\n{player1.name} and {player2.name} both chose {player1.gesture.name}!')
            print('It\'s a tie! No points awarded.')
        # if the players choose different gestures, it will compare the gestures and award a point to the winner
        elif player1.gesture.name != player2.gesture.name:
            if player1.gesture.name == 'rock':
                if player2.gesture.name == Rock().beats[0]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                elif player2.gesture.name == Rock().beats[1]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                else:
                    print(f'{player2.name} wins the round!')
                    player2.score += 1
            elif player1.gesture.name == 'paper':
                if player2.gesture.name == Paper().beats[0]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                elif player2.gesture.name == Paper().beats[1]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                else:
                    print(f'{player2.name} wins the round!')
                    player2.score += 1
            elif player1.gesture.name == 'scissors':
                if player2.gesture.name == Scissors().beats[0]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                elif player2.gesture.name == Scissors().beats[1]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                else:
                    print(f'{player2.name} wins the round!')
                    player2.score += 1
            elif player1.gesture.name == 'lizard':
                if player2.gesture.name == Lizard().beats[0]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                elif player2.gesture.name == Lizard().beats[1]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                else:
                    print(f'{player2.name} wins the round!')
                    player2.score += 1
            elif player1.gesture.name == 'spock':
                if player2.gesture.name == Spock().beats[0]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                elif player2.gesture.name == Spock().beats[1]:
                    print(f'{player1.name} wins the round!')
                    player1.score += 1
                else:
                    print(f'{player2.name} wins the round!')
                    player2.score += 1
# it will have a method that will play the game
    def play_game(self, num_wins):
        # it will run a loop that will continue until one of the players reaches 3 points
        while self.players[0].score < num_wins and self.players[1].score < num_wins:
            # it will call the choose_gesture method for both players
            self.players[0].choose_gesture()
            print(f'{self.players[0].name} chose {self.players[0].gesture.name}!')
            sleep(1)
            self.players[1].choose_gesture()
            print(f'{self.players[1].name} chose {self.players[1].gesture.name}!')
            sleep(1)
            # it will call the compare_gestures method
            self.compare_gestures(player1=self.players[0], player2=self.players[1])
            # it will print the scores
            print(f'\n{self.players[0].name}\'s score: {self.players[0].score}')
            print(f'{self.players[1].name}\'s score: {self.players[1].score}')
            sleep(1)
        # it will print the winner
        if self.players[0].score == num_wins:
            print(f'\n{self.players[0].name} wins the game!')
        elif self.players[1].score == num_wins:
            print(f'\n{self.players[1].name} wins the game!')
# it will have a method that will display the final score and the winner
    def display_final_score(self):
        print(f'{self.players[0].name}\'s score: {self.players[0].score}')
        print(f'{self.players[1].name}\'s score: {self.players[1].score}')
        if self.players[0].score > self.players[1].score:
            print(f'\n{self.players[0].name} wins the game!')
        else:
            print(f'\n{self.players[1].name} wins the game!')
# it will have a method that will ask the user if they would like to play again
    def play_again(self):
        print('\nWould you like to play again?')
        print('1. Yes')
        print('2. No')
        choice = int(input('\nPlease enter the number of your choice: '))
        if choice == 1:
            print('\nStarting a new game...')
            return True
        elif choice == 2:
            print('\nThank you for playing!')
            return False
        else:
            print('Invalid choice. Please try again.')
            self.play_again()
