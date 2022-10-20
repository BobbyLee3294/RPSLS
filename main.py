# this file is used to run the game
from time import sleep
# we will also import the game_logic file and the create_gestures method from the gestures folder
import game_logic
from gestures.creategesturelist import create_gestures
# we will create a main function that will run the game
def main():
    # we will call the display_gretting method from the game_logic file
    game_logic.display_greeting()
    # we will call the create_gestures method from the creategesturelist file
    gestures = create_gestures()
    # we will call the create_game_mode method from the game_logic file
    mode = game_logic.create_game_mode()
    # we will call the create_win_goal method from the game_logic file
    wins = game_logic.create_win_goal()
    # we will create a variable that will hold the list of players created by the create_players method from the game_logic file
    players = game_logic.create_players(mode)
    # we will create a while loop that will run until one of the players has reached the number of wins
    while players[0].score < wins and players[1].score < wins:
        # we will call the choose_gestures method from the each player given from the players list
        players[0].choose_gesture()
        print(f'\n{players[0].name} chose {players[0].choice.name}.')
        sleep(2)
        players[1].choose_gesture()
        print(f'\n{players[1].name} chose {players[1].choice.name}.')
        sleep(2)
        # we will call the compare_gestures method from the game_logic file
        game_logic.compare_gestures(players)
    # we will call the display_final_score method from the game_logic file
    game_logic.display_final_score(players)
    # ask the user if they would like to play again
    if game_logic.play_again():
        main()
# calling the main function to run the game
main()