# this file is used to run the game
import game_logic
# we will create a main function that will run the game
def main():
    # we will create a new game object
    game = game_logic.Game()
    # we will call the display_greeting method
    game.display_greeting()
    # we will call the display_rules method
    game.display_rules()
    # we will create a variable that will hold the game mode
    mode = game.create_game_mode()
    # we will create a variable that will hold the wins goal
    num_wins = game.create_win_goal()
    # we will create a list that will hold the players
    players = game.create_players(mode)
    # we call the play_game method
    game.play_game(num_wins)
    # we will call the display_final_score method
    game.display_final_score()
    # we will call the play_again method
    if game.play_again():
        main()
# calling the main function to run the game
main()