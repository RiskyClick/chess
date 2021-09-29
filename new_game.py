from board import *
from player import *
from peices import *

class new_game():
    def __init__(self, color):
        self.board = board()
        if color == 'white':
            pass
        self.white = player('white')
        self.black = player('black')

    def select_peice(player):
        while True:
            select = input()
            if not player.owmership(select):
                print("You Selected {} which is not your peice, try again: ".format(select))
            else:
                return player.get_peice(select)
            
    def move_to(peice):
        pass

    def game_flow(self):
        self.board.draw_board(self.white.peices, self.black.peices)
        if self.white.turn:
            print("whites turn, enter the peice you want to move: ")
            peice = self.select_peice(player)
            print("You selected the {} at {}".format(peice.title, peice.position))
            print("Enter the location you want to move to: ")
            move = self.move_to(peice)

        #draw the board
        #whos turn is it
        
        #person whos turn it is select peaice
        #location to move peice



