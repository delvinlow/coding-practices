import unittest
from Solution import Solution

class TestValidParentheses(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_string_returns_true(self):
        input_str = ""
        self.assertTrue(self.solution.isValid(input_str))
        
    def test_single_round_bracket_returns_false(self):
        input_str = "("
        self.assertFalse(self.solution.isValid(input_str))

    def test_single_square_bracket_returns_false(self):
        input_str = "["
        self.assertFalse(self.solution.isValid(input_str))

    def test_single_curly_bracket_returns_false(self):
        input_str = "["
        self.assertFalse(self.solution.isValid(input_str))

    def test_pair_round_bracket_returns_true(self):
        input_str = "()"
        self.assertTrue(self.solution.isValid(input_str))

    def test_pair_square_bracket_returns_true(self):
        input_str = "[]"
        self.assertTrue(self.solution.isValid(input_str))

    def test_pair_curly_bracket_returns_true(self):
        input_str = "{}"
        self.assertTrue(self.solution.isValid(input_str))

    def test_valid_combinations_returns_true(self):
        input_str = "{}[]()"
        self.assertTrue(self.solution.isValid(input_str))

    def test_valid_nested_combinations_returns_true(self):
        input_str = "([{}])"
        self.assertTrue(self.solution.isValid(input_str))

    def test_invalid_nested_combinations_on_right_returns_false(self):
        input_str = "([{}]"
        self.assertFalse(self.solution.isValid(input_str))

    def test_invalid_nested_combinations_on_left_returns_false(self):
        input_str = "[{}])"
        self.assertFalse(self.solution.isValid(input_str))


        
# if __name__ == "__main__":
#     unittest.main()