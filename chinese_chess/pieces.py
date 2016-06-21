class Piece(object):
    def __init__(self):
        self.role = str(self.__class__.__name__)

    def __str__(self):
        return str(self.role)

    def next(self, cur):
        return []

    def move_to(self, cur, destination):
        pass


# 将帅
class King(Piece):
    def __init__(self):
        super().__init__()

    def next(self, cur):
        return []

    def move_to(self, cur, destination):
        pass


# 士
class Guard(Piece):
    def __init__(self):
        super().__init__()


# 士
class Cannon(Piece):
    def __init__(self):
        super().__init__()


# 相
class Bishop(Piece):
    def __init__(self):
        super().__init__()


# 马
class Knight(Piece):
    def __init__(self):
        super().__init__()


# 车
class Rook(Piece):
    def __init__(self):
        super().__init__()


class Pawn(Piece):
    def __init__(self):
        super().__init__()
