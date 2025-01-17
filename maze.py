from windows import Window
from cell import Cell
import time
import random
import inspect

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if seed:
            random.seed(seed)

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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        

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
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell((len(self._cells) - 1), (len(self._cells[-1]) - 1))

    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            need_to_visit = []
            if i > 0:  # Check cell above
                if not self._cells[i - 1][j].visited:
                    need_to_visit.append((i - 1, j))
            if i < len(self._cells) - 1:  # Check cell below
                if not self._cells[i + 1][j].visited:
                    need_to_visit.append((i + 1, j))
            if j > 0:  # Check cell left
                if not self._cells[i][j - 1].visited:
                    need_to_visit.append((i, j - 1))
            if j < len(self._cells[0]) - 1:  # Check cell right
                if not self._cells[i][j + 1].visited:
                    need_to_visit.append((i, j + 1))
            if len(need_to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = random.randrange(len(need_to_visit))
                next_i, next_j = need_to_visit[direction]
                if next_i == i - 1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[next_i][next_j].has_bottom_wall = False
                    #below
                if next_i == i + 1:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[next_i][next_j].has_top_wall = False
                    #left
                if next_j == j - 1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[next_i][next_j].has_right_wall = False
                    #right
                if next_j == j + 1:
                    self._cells[i][j].has_right_wall = False
                    self._cells[next_i][next_j].has_left_wall = False
                self._break_walls_r(next_i, next_j)


    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self):
        self._solve_r(0,0)

    def _solve_r(self, i, j):


    """def _get_unvisited_neighbors(self, i, j):
    neighbors = []
    if i > 0 and not self._cells[i - 1][j].visited:  # Above
        neighbors.append((i - 1, j))
    if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:  # Below
        neighbors.append((i + 1, j))
    if j > 0 and not self._cells[i][j - 1].visited:  # Left
        neighbors.append((i, j - 1))
    if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:  # Right
        neighbors.append((i, j + 1))
    return neighbors"""


    """def _break_wall_between(self, i1, j1, i2, j2):
    if i2 == i1 - 1:  # Above
        self._cells[i1][j1].has_top_wall = False
        self._cells[i2][j2].has_bottom_wall = False
    elif i2 == i1 + 1:  # Below
        self._cells[i1][j1].has_bottom_wall = False
        self._cells[i2][j2].has_top_wall = False
    elif j2 == j1 - 1:  # Left
        self._cells[i1][j1].has_left_wall = False
        self._cells[i2][j2].has_right_wall = False
    elif j2 == j1 + 1:  # Right
        self._cells[i1][j1].has_right_wall = False
        self._cells[i2][j2].has_left_wall"""

            

        


        
