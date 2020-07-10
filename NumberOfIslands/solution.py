class Solution:
    def num_islands(self, grid):
        if not grid:
            return 0
        self.initialize(grid)
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if type(self.grid[row][col]) is not str:
                        raise TypeError
                self.visit_grid_cell(row, col)
        return self.count_of_islands
    
    def initialize(self, grid):
        self.num_rows = len(grid)
        self.num_cols = len(grid[0])
        self.grid = grid
        self.has_visited = [[False for col in range(self.num_cols)] for col in range(self.num_rows)]
        self.count_of_islands = 0

    def visit_grid_cell(self, row_index, col_index):
        if not self.has_visited[row_index][col_index]:
            if self.is_land(self.grid[row_index][col_index]):
                self.count_of_islands += 1
                self.visit_neighbours(row_index, col_index)

    def visit_neighbours(self, row, col):
        for i in (row - 1, row, row + 1):
            for j in (col - 1, col, col + 1):
                if self.is_within_grid(i, j) and self.is_neighbour(row, col, i, j) and not self.has_visited[i][j] and self.is_land(self.grid[i][j]):
                    self.has_visited[i][j] = True
                    self.visit_neighbours(i, j)

    def is_land(self, cell_value):
        return cell_value == "1"

    def is_neighbour(self, current_row, current_col, adjacent_row, adjacent_col):
        return current_row == adjacent_row or current_col == adjacent_col

    def is_within_grid(self, row_index, col_index):
        return (row_index < self.get_num_rows()) and (row_index >= 0) and (col_index < self.get_num_cols()) and (col_index >= 0)

    def get_num_cols(self):
        return self.num_cols

    def get_num_rows(self):
        return self.num_rows