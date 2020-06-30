import unittest
from solution import Solution

class TestMaximumSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list_return_none(self):
        input_nums = []
        output_nums = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_nums, None)

    def test_positive_sequence_return_its_sum(self):
        input_nums = [1, 2, 3, 4, 5]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, 15)

    def test_reversed_positive_sequence_return_its_sum(self):
        input_nums = [5, 4, 3, 2, 1]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, 15)

    def test_single_negative_element_sequence_return_itself(self):
        input_nums = [-2]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, -2)

    def test_single_positive_element_sequence_return_itself(self):
        input_nums = [2]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, 2)

    def test_short_mixed_sequence_return_maximum_subarray_sum(self):
        input_nums = [-2, 1, -3, 4]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, 4)

    def test_mixed_sequence_return_maximum_subarray_sum(self):
        input_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, 6)

    def test_negative_sequence_return_first_element(self):
        input_nums = [-1, -2, -3, -4, -5]
        output_sum = self.solution.max_sub_array(input_nums)
        self.assertEqual(output_sum, -1)