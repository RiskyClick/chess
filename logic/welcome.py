from chess.logic.new_game import *
class welcome_screen():
    print("+++++++Welcome+++++++")
    print("If you would like to \nplay a game of chess")
    print("Press Y")
    choice = 'y'
    if choice == 'y' or choice == 'Y':
        print("If you want to be black press b")
        choice = 'input()'
        if choice == 'b':
            pass
        print("Have fun!")
        new_game = new_game('white')
        new_game.game_flow()

    else:
        print("Goodbye!")