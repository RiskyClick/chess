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
            #select = input()
            select = 'A1'
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

    def follows_rule(self, peice, location):
        return peice.rule(location, self.board)

    def change_location(self, peice, location):
        print("The {} at {} will move to {}".format(peice.title, peice.position, location))
        peice.position = location
        print("The {} is now at {}".format(peice.title, peice.position))

    def open_space(self, location):
        if (location in self.white.peices and self.white.turn) \
        or (location in self.black.peices and self.black.turn):
            return False
        else:
            return True

    def r_shift(self, peice, location):
        up_down = False
        up = False
        left = False
        rreal = self.board.positions.get(peice.position)
        temp = rreal
        lreal = self.board.positions.get(location)
        if rreal[1] == lreal[1]:
            up_down = True
            if rreal[0] > lreal[0]:
                up = True
        elif rreal[1] > lreal[1]:
            left = True

        if up:
            while temp[0] >= lreal[0]:
                print("{} rreal".format(rreal))
                print("{} twmp".format(temp))
                temp[0] -= 1
                for i in self.white.peices:
                    print("{} i.pos".format(i.position))
                    print("{} twmp".format(temp))
                    print("{} rreal".format(rreal))
                    print("{} self.board.positions.get(i.position)".format(self.board.positions.get(i.position)))
                    if temp == self.board.positions.get(i.position):
                        return False
                print("forloop for black")
                for i in self.black.peices:
                    print(i.title)
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
        input()
        print("this should be the end of it")





    def b_shift(self, peice, location):
        pass

    def p_shift(self, peice, location):
        pass

    def k_shift(self, peice, location):
        pass

    def q_shift(self, peice, location):
        pass

    def blocked(self, peice, location):
        if peice.title == 'k':
            return True
        block_call = {
            "R": self.r_shift(peice, location),
            "B": self.b_shift(peice, location),
            "K": self.k_shift(peice, location),
            "Q": self.q_shift(peice, location),
            "p": self.p_shift(peice, location)
        }
        return block_call.get(peice.title)

    def move_to(self, peice, color):
        print("Enter the location you want to move {} to: ".format(peice.title))
        while True:
            #location = input()
            location = 'A4'
            if self.on_board(location) and self.open_space(location):
                if self.follows_rule(peice, location):
                    if self.blocked(peice, location):
                        self.change_location(peice, location)
                        return peice
                    else:
                        print("Your {} is blocked".format(peice.title))
                else:
                    print("{} cant make that move".format(peice.title))

            else:
                print("{} is not on the board. What the fuck you doing bro".format(location))
                print("Pick again")
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



