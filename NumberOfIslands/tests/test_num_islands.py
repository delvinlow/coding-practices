import unittest
from solution import Solution

class TestNumberOfIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_grid_returns_zero(self):
        input_grid = []
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 0)

    def test_single_land_grid_returns_one(self):
        input_grid = [["1"]]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 1)

    def test_single_water_grid_returns_zero(self):
        input_grid = [["0"]]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 0)

    def test_double_adjacent_land_grid_returns_one(self):
        input_grid = [["1"], ["1"]]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 1)
        
    def test_four_land_water_grid_returns_two(self):
        input_grid = [["1", "0"], ["0", "1"]]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 2)

    def test_non_string_inputs_throw_errors(self):
        input_grid = [["1", "0", "1", "0", "1", "0", "0"], 
                        [0, 0, 0, 0, 0, 0 ,0 , 0]]
        with self.assertRaises(TypeError):
            self.solution.num_islands(input_grid)

    def test_single_connected_island_returns_one(self):
        input_grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 1)

    def test_three_connected_islands_return_three(self):
        input_grid = [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ]
        count_of_islands = self.solution.num_islands(input_grid)
        self.assertEqual(count_of_islands, 3)