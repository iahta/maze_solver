from windows import Window
from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._validate_dimensions()
        self._create_cells()
        self._break_entrance_and_exit()
        

    def _validate_dimensions(self):
        if self.num_rows <= 0:
            raise ValueError(f"Number of rows must be positive. Got: {self.num_rows}")
        if self.num_cols <= 0:
            raise ValueError(f"Number of columns must be positive. Got: {self.num_cols}")
    """boots
    more pythonic
    def _create_cells(self):
    # Create the 2D grid using list comprehension
    self._cells = [[Cell(self.win) for _ in range(self.num_rows)] 
                   for _ in range(self.num_cols)]
    
    # Draw cells using enumerate to get indices
    for i, column in enumerate(self._cells):
        for j, cell in enumerate(column):
            self._draw_cell(i, j)"""

    def _create_cells(self):
        self._cells = []
        for _ in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                column.append(Cell(self.win))
            self._cells.append(column)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                    self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        x_pos = self.x1 + (j * self.cell_size_x)  # j is the column number
        y_pos = self.y1 + (i * self.cell_size_y)  # i is the row number     
        self._cells[i][j].draw(x_pos, y_pos, (x_pos + self.cell_size_x), (y_pos + self.cell_size_y))
        if self.win is not None:
            self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        if len(self._cells) == 1 and len(self._cells[len(self._cells) - 1]) == 1:
            self._cells[0][0].has_bottom_wall = False
            self._draw_cell(0, 0)
        else:
            self._draw_cell(0, 0)
            self._cells[-1][-1].has_bottom_wall = False
            self._draw_cell((len(self._cells) - 1), (len(self._cells[-1]) - 1))
