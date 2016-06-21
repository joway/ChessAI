"""
9 * 10
"""
import tkinter as tk

from chinese_chess.pieces import Rook, Knight, Bishop, Guard, King, Cannon, Pawn


class Board(tk.Frame):
    def __init__(self, parent, rows=10, columns=9, size=48):
        tk.Frame.__init__(self, parent)

        # 对手
        self.king = False
        self.general = True

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color = "white"
        self.bg_color = 'bisque'
        self.board = self.init_board
        # 是否选中
        self.status = False
        self.selected = None

        canvas_width = columns * size
        canvas_height = rows * size

        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width + 1, height=canvas_height + 1,
                                background=self.bg_color)

        self.canvas.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        self.init_canvas()

    @property
    def init_board(self):
        board = [[0 for col in range(9)] for row in range(10)]

        # 注意,每个子都是一个独立实例,不能连等

        # 车
        board[0][0] = Rook(self.king)
        board[0][8] = Rook(self.king)
        board[9][0] = Rook(self.general)
        board[9][8] = Rook(self.general)

        # 马
        board[0][1] = Knight(self.king)
        board[0][7] = Knight(self.king)
        board[9][1] = Knight(self.general)
        board[9][7] = Knight(self.general)

        # 相
        board[0][2] = Bishop(self.king)
        board[0][6] = Bishop(self.king)
        board[9][2] = Bishop(self.general)
        board[9][6] = Bishop(self.general)

        # 士
        board[0][3] = Guard(self.king)
        board[0][5] = Guard(self.king)
        board[9][3] = Guard(self.general)
        board[9][5] = Guard(self.general)

        # 将帅
        board[0][4] = King(self.king)
        board[9][4] = King(self.general)

        # 炮
        board[2][1] = Cannon(self.king)
        board[2][7] = Cannon(self.king)
        board[7][1] = Cannon(self.general)
        board[7][7] = Cannon(self.general)

        # 兵卒
        for i in range(0, 9, 2):
            board[3][i] = Pawn(self.king)
            board[6][i] = Pawn(self.general)
        return board

    def init_canvas(self):
        for row in range(0, self.rows):
            # cell:
            self.canvas.create_line(0, row * self.size, self.columns * self.size, row * self.size)
            for column in range(0, self.columns):
                self.canvas.create_line(column * self.size, 0, column * self.size, self.rows * self.size)
                # init pieces
                if self.piece(row, column):
                    oval_id = self.canvas.create_oval(column * self.size, row * self.size,
                                                      (column + 1) * self.size, (row + 1) * self.size, fill='#eee000',
                                                      tags=(self.piece(row, column).uuid, "piece"))
                    text_id = self.canvas.create_text((column + 1 / 2) * self.size, (row + 1 / 2) * self.size,
                                                      text=self.piece(row, column).translate(),
                                                      tags=(self.piece(row, column).uuid, "piece"),
                                                      anchor="c", fill=self.piece(row, column).color(),
                                                      font="Purisa 26")
                    self.canvas.tag_bind(oval_id, "<Button-1>", self.handle_click)
                    self.canvas.tag_bind(text_id, "<Button-1>", self.handle_click)

                    # this binding will cause a refresh if the user interactively
                    # changes the window size
                    # self.canvas.bind("<Configure>", self.refresh)
                else:
                    oval_id = self.canvas.create_rectangle(column * self.size, row * self.size,
                                                           (column + 1) * self.size, (row + 1) * self.size,
                                                           tags="square", fill=self.bg_color)

                    self.canvas.tag_bind(oval_id, "<Button-1>", self.handle_place)

        self.canvas.create_line(0, self.rows * self.size, self.columns * self.size,
                                self.rows * self.size)

        self.canvas.create_line(self.columns * self.size, 0, self.columns * self.size,
                                self.rows * self.size)
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def handle_click(self, event):
        row, col = self.trans_to_row_col(event=event)
        piece = self.piece(row, col)
        self.selected = piece
        self.status = True

    def handle_place(self, event):
        row, col = self.trans_to_row_col(event=event)
        piece = self.piece(row, col)
        if self.status:
            # refresh
            self.canvas.delete(self.selected.uuid)
            self.selected = None
            self.status = False

    def trans_to_row_col(self, event):
        # 注意, 这边需要对坐标x,y 与 行列 反一下, 并不是直接对应关系
        x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
        return int(y // self.size), int(x // self.size)

    def __str__(self):
        return str(self.board)

    def piece(self, row, col):
        return self.board[row][col]

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


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
if __name__ == "__main__":
    root = tk.Tk()
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
