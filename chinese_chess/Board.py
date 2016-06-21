"""
9 * 10
"""
from chinese_chess.pieces import Rook, Knight, Bishop, Guard, King, Cannon, Pawn


class Board(object):
    def __init__(self):
        self.board = self.init_board

    @property
    def init_board(self):
        board = [[0 for col in range(9)] for row in range(10)]
        board[0][0] = board[0][8] = board[9][0] = board[9][8] = Rook()
        board[0][1] = board[0][7] = board[9][1] = board[9][7] = Knight()
        board[0][2] = board[0][6] = board[9][2] = board[9][6] = Bishop()
        board[0][3] = board[0][5] = board[9][3] = board[9][5] = Guard()
        board[0][4] = board[9][4] = King()
        board[2][1] = board[2][7] = board[7][1] = board[7][7] = Cannon()

        for i in range(0, 9, 2):
            board[3][i] = board[6][i] = Pawn()
        return board

    def __str__(self):
        return str(self.board)

    def cell(self, role):
        while len(role) < 6:
            role += " "
        return role

    def show(self):
        for index, value in enumerate(self.board):
            print([self.cell(str(x)) for x in value])
            if index == 4:
                print("-" * 100)
                print("-" * 100)


boa = Board()
boa.show()
