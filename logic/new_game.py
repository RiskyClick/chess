from chess.items.board import *
from chess.items.player import *
from chess.items.peices import *

class new_game():
    def __init__(self, color):
        self.board = board()
        if color == 'white':
            pass
        self.white = player('white')
        self.black = player('black')

    def select_peice(self, color):
        while True:
            select = input()
            peice = self.white.ownership(select)
            if color == 'w':
                if peice == 'False':
                    print("You Selected {} which is not your peice, try again: ".format(select))
                else:
                    print("You selected the {} at {}".format(peice.title, peice.position))
                    return peice
            else:
                if peice == 'False':
                    print("You Selected {} which is not your peice, try again: ".format(select))
                else:
                    print("You selected the {} at {}".format(peice.title, peice.position))
                    return peice

    def on_board(self, location):
        if location in self.board.positions:
            return True
        else:
            return False

    def not_blocked(self, peice, location):
        return True

    def change_location(self, peice, location):
        print("The {} at {} will move to {}".format(peice.title, peice.position, location))
        peice.position = location
        print("The {} is now at {}".format(peice.title, peice.position))

    def move_to(self, peice, color):
        print("Enter the location you want to move {} to: ".format(peice.title))
        while True:
            location = input()
            if self.on_board(location):
                if self.not_blocked(peice, location):
                    self.change_location(peice, location)
                    return peice

            else:
                print("{} is not on the board. What the fuck you doing bro".format(location))
                print("Pick again")
        #check if its on board.
        #chck if its open space
        #chekc if its the openes peice
        #check peice rules
        #check if blocked

    def game_flow(self):
        self.board.draw_board(self.white.peices, self.black.peices)
        if self.white.turn:
            print("whites turn, enter the peice you want to move: ")
            peice = self.select_peice('w')
            self.move_to(peice, 'w')
            self.board.draw_board(self.white.peices, self.black.peices)

        #draw the board
        #whos turn is it
        
        #person whos turn it is select peaice
        #location to move peice



