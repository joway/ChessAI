from random import Random


def gen_uuid(length=8):
    uuid = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    total_length = len(chars) - 1
    random = Random()
    for i in range(length):
        uuid += chars[random.randint(0, total_length)]
    return uuid


class Piece(object):
    def __init__(self, owner):
        self.role = str(self.__class__.__name__)
        self.map = {
            "King": "将",
            "Guard": "士",
            "Cannon": "炮",
            "Bishop": "相",
            "Knight": "马",
            "Rook": "车",
            "Pawn": "兵"
        }
        self.owner = owner
        self.uuid = gen_uuid()

    def __str__(self):
        return str(self.role)

    def next(self, cur):
        return []

    def move_to(self, cur, destination):
        pass

    def translate(self):
        return self.map.get(self.__class__.__name__, None)

    def color(self):
        if self.owner:
            return "red"
        else:
            return "black"


# 将帅
class King(Piece):
    def __init__(self, owner):
        super().__init__(owner)

    def next(self, cur):
        return []

    def move_to(self, cur, destination):
        pass


# 士
class Guard(Piece):
    def __init__(self, owner):
        super().__init__(owner)


# 士
class Cannon(Piece):
    def __init__(self, owner):
        super().__init__(owner)


# 相
class Bishop(Piece):
    def __init__(self, owner):
        super().__init__(owner)


# 马
class Knight(Piece):
    def __init__(self, owner):
        super().__init__(owner)


# 车
class Rook(Piece):
    def __init__(self, owner):
        super().__init__(owner)


# 兵
class Pawn(Piece):
    def __init__(self, owner):
        super().__init__(owner)

print(gen_uuid())