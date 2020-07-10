import unittest
from solution import Solution
from unittest.mock import patch

class TestWithinGrid(unittest.TestCase):
    @patch("solution.Solution")
    def test_valid_cell_at_origin_returns_true(self, mockSolution):
        mockSolution.num_rows.return_value = 3
        mockSolution.num_cols.return_value = 4
        within_grid = mockSolution.is_within_grid(0, 0)
        self.assertTrue(within_grid)

    @patch("solution.Solution.get_num_cols", return_value = 4)
    @patch("solution.Solution.get_num_rows", return_value = 3)
    def test_invalid_row_lower_bound_returns_false(self, mock_get_num_rows, mock_get_num_cols):
        within_grid = Solution().is_within_grid(-1, 0)
        self.assertFalse(within_grid)

    @patch("solution.Solution.get_num_cols", return_value = 4)
    @patch("solution.Solution.get_num_rows", return_value = 3)
    def test_invalid_row_upper_bound_returns_false(self, mock_get_num_rows, mock_get_num_cols):
        within_grid = Solution().is_within_grid(3, 4)
        self.assertFalse(within_grid)

    @patch("solution.Solution.get_num_cols", return_value = 4)
    @patch("solution.Solution.get_num_rows", return_value = 3)
    def test_invalid_row_and_col_upper_bounds_returns_false(self, mock_get_num_rows, mock_get_num_cols):
        within_grid = Solution().is_within_grid(4, 5)
        self.assertFalse(within_grid)

    @patch("solution.Solution.get_num_cols", return_value = 4)
    @patch("solution.Solution.get_num_rows", return_value = 3)
    def test_within_bound_returns_false(self, mock_get_num_rows, mock_get_num_cols):
        within_grid = Solution().is_within_grid(2, 2)
        self.assertTrue(within_grid)