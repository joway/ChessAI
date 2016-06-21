import tkinter as tk

from chinese_chess.Board import Board


class GameBoard(tk.Frame):
    def __init__(self, parent, rows=10, columns=9, size=32):
        tk.Frame.__init__(self, parent)
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color = "yellow"
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def add_piece(self, name, text, row=0, column=0):
        id = self.canvas.create_text(row, column, text=text, tags=(name, "piece"), anchor="c")
        # self.canvas.tag_bind(id, "<Button-1>", log)
        self.place_piece(name, row, column)

    def place_piece(self, name, row, column):
        self.pieces[name] = (row, column)
        x = (column * self.size) + int(self.size / 2)
        y = (row * self.size) + int(self.size / 2)
        self.canvas.coords(name, x, y)

    def refresh(self, event):
        # Redraw the board, possibly in response to window being resized
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=self.color, tags="square")
        for name in self.pieces:
            self.place_piece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    boa = Board(root)
    boa.show()
    for i in range(0, len(boa.board)):
        for j in range(0, len(boa.board[i])):
            if boa.board[i][j] is not 0:
                board.add_piece("player", boa.board[i][j], i*25, j*25)
    root.mainloop()
