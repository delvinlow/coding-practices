import unittest
from generate_matrix import generate_matrix


class TestGenerateMatrix(unittest.TestCase):
    def test_generate_single_cell_matrix(self):
        grid = generate_matrix(1)
        self.assertEqual([[1]], grid)

    def test_generate_three_by_three_matrix_in_spiral_order(self):
        grid = generate_matrix(3)
        self.assertEqual([[1, 2, 3], [8, 9, 4], [7, 6, 5]], grid)

    def test_generate_four_by_four_matrix_in_spiral_order(self):
        grid = generate_matrix(4)
        self.assertEqual([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]], grid)