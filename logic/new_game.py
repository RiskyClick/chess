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
            select = 'D4'
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
        if peice.position == location:
            return False
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
        rreal = self.board.positions.get(peice.position).copy()
        lreal = self.board.positions.get(location)
        if rreal[1] == lreal[1]:
            up_down = True
            if rreal[0] > lreal[0]:
                up = True
        elif rreal[1] > lreal[1]:
            left = True

        if up:
            while rreal[0] != lreal[0]:
                rreal[0] -= 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for j in self.black.peices:
                    if rreal == self.board.positions.get(j.position):
                        return False
            return True

        elif up_down:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal[0] != lreal[0]:
                rreal[0] += 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True

        elif left:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal[1] != lreal[1]:
                rreal[1] -= 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True

        else:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal[1] != lreal[1]:
                rreal[1] += 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True


    def b_shift(self, peice, location):
        up_left = False
        up_right = False
        down_left = False
        rreal = self.board.positions.get(peice.position).copy()
        lreal = self.board.positions.get(location)
        if rreal[0] > lreal[0]:
            if rreal[1] > lreal[1]:
                up_left = True
            else:
                up_right = True
        elif rreal[1] > lreal[1]:
            down_left = True

        if up_left:
            while rreal != lreal:
                rreal[0] -= 1
                rreal[1] -= 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True
        elif up_right:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal != lreal:
                rreal[0] -= 1
                rreal[1] += 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True

        elif down_left:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal != lreal:
                rreal[0] += 1
                rreal[1] -= 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True

        else:
            rreal = self.board.positions.get(peice.position).copy()
            while rreal != lreal:
                rreal[0] += 1
                rreal[1] += 1
                for i in self.white.peices:
                    if rreal == self.board.positions.get(i.position):
                        return False
                for i in self.black.peices:
                    if rreal == self.board.positions.get(i.position) and rreal != lreal:
                        return False
            return True

    def p_shift(self, peice, location):
        rreal = self.board.positions.get(peice.position).copy()
        lreal = self.board.positions.get(location)
        if abs(rreal[1] - lreal[1]) == 1:
            return True
        else:
            if rreal[0] > lreal[0]:
                while rreal[0] != lreal[0]:
                    rreal -= 1
                    for i in self.white.peices:
                        if rreal == self.board.positions.get(i.position):
                            return False
                    for j in self.black.peices:
                        if rreal == self.board.positions.get(j.position):
                            return False
                return True
            else:
                while rreal[0] != lreal[0]:
                    rreal += 1
                    for i in self.white.peices:
                        if rreal == self.board.positions.get(i.position):
                            return False
                    for j in self.black.peices:
                        if rreal == self.board.positions.get(j.position):
                            return False
                return True

    def K_shift(self, peice, location):
        if peice.owner == 'white':
            return False if location in self.white.peices else True
        else:
            return False if location in self.black.peices else True

    def q_shift(self, peice, location):
        rreal = self.board.positions.get(peice.position).copy()
        lreal = self.board.positions.get(location)
        if rreal[0] == lreal[0] or rreal[1] == lreal[1]:
            return self.r_shift(peice, location)
        else:
            return self.b_shift(peice, location)

    def blocked(self, peice, location):
        if peice.title == 'k':
            return True
        block_call = {
            "R": self.r_shift(peice, location),
            "B": self.b_shift(peice, location),
            "K": self.K_shift(peice, location),
            "Q": self.q_shift(peice, location),
            "p": self.p_shift(peice, location)
        }
        return block_call.get(peice.title)

    def move_to(self, peice, color):
        print("Enter the location you want to move {} to: ".format(peice.title))
        while True:
            location = input()
            #location = 'A4'
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




