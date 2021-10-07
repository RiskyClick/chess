from chess.items.board import *
class peices():
    def __init__(self, title, owner, position):
        self.title = title
        self.owner = owner
        self.position = position
        self.first_move = True


    def rule(self, location, board):
        rule_call = {
            "R": self.rook(location, board),
            "B": self.bishop(location, board),
            "k": self.knight(location, board),
            "K": self.king(location, board),
            "Q": self.queen(location, board),
            "p": self.pawn(location, board)
        }
        return rule_call.get(self.title)

    def rook(self, location, board):
        current = board.positions.get(self.position)
        loc = board.positions.get(location)
        if current[0] == loc[0] or current[1] == loc[1]:
            return True
        else:
            return False

    def bishop(self, location, board):
        current = board.positions.get(self.position)
        loc = board.positions.get(location)
        if abs(current[0] - loc[0]) == abs(current[1] - loc[1]):
            return True
        else:
            return False

    def knight(self, location, board):
        current = board.positions.get(self.position)
        loc = board.positions.get(location)
        first = abs(current[0] - loc[0])
        second = abs(current[1] - loc[1])
        if (first == 1 and second == 2) or (first == 2 and second == 1):
            return True
        else:
            return False

    def king(self, location, board):
        current = board.positions.get(self.position)
        loc = board.positions.get(location)
        first = abs(current[0] - loc[0])
        second = abs(current[1] - loc[1])
        if first > 1 or second > 1:
            return False
        else:
            return True

    def queen(self, location, board):
        if self.rook(location, board) or self.bishop(location, board):
            return True
        else:
            return False

    def pawn(self, location, board):
        current = board.positions.get(self.position)
        loc = board.positions.get(location)
        first = abs(current[0] - loc[0])
        second = abs(current[1] - loc[1])
        if second < 1:
            if first == 1:
                return True
            elif self.first_move and first == 2:
                return True
            else:
                return False
        else:
            return board.positions.get(location)

    def get_title(self):
        return self.title

    def get_position(self):
        return self.position

    def get_owner(self):
        return self.owner