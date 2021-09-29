from peices import *
starting_black = [
    ['R', 'A8'],
    ['B', 'B8'],
    ['k', 'C8'],
    ['Q', 'D8'],
    ['K', 'E8'],
    ['k', 'F8'],
    ['B', 'G8'],
    ['R', 'H8'],
    ['p', 'A7'],
    ['p', 'B7'],
    ['p', 'C7'],
    ['p', 'D7'],
    ['p', 'E7'],
    ['p', 'F7'],
    ['p', 'G7'],
    ['p', 'H7'],
]

starting_white = [
    ['R', 'A1'],
    ['B', 'B1'],
    ['k', 'C1'],
    ['K', 'D1'],
    ['Q', 'E1'],
    ['k', 'F1'],
    ['B', 'G1'],
    ['R', 'H1'],
    ['p', 'A2'],
    ['p', 'B2'],
    ['p', 'C2'],
    ['p', 'D2'],
    ['p', 'E2'],
    ['p', 'F2'],
    ['p', 'G2'],
    ['p', 'H2'],
]

class player:
    def __init__(self, color):
        self.color = color
        self.peices = []
        self.turn = False
        if self.color == 'black':
            for i in starting_black:
                self.peices.append(peices(i[0], self.color, i[1]))
        else:
            self.turn = True
            for i in starting_white:
                self.peices.append(peices(i[0], self.color, i[1]))

    def get_color(self):
        print(self.color)

    def ownership(self, input):
        for i in self.peices:
            if i.position == input:
                return i
        return False

    def print_peices(self):
        for i in self.peices:
            print("Title: {} Pos: {}".format(i.title, i.position))