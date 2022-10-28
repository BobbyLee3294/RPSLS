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
    # we will call the run_game method
    game.run_game()
# calling the main function to run the game
main()