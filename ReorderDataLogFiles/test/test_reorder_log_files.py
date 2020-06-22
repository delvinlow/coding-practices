import unittest

from Solution import Solution

class TestReorderLogFiles(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_item_list_returns_itself(self):
        self.input_list = ["dig1 8 1 5 1"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEqual(self.input_list, output_list)

    def test_two_items_digit_list_returns_in_same_order(self):
        self.input_list = ["dig2 3 6", "dig1 8 1 5 1"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEqual(self.input_list, output_list)

    def test_mixed_letter_digit_list_returns_letters_first(self):
        self.input_list = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["let1 art can", "dig1 8 1 5 1", "dig2 3 6"])

    def test_mixed_letter_digit_list_returns_letters_first_with_sorted_letters(self):
        self.input_list = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"])

    def test_mixed_letter_digit_list_returns_letters_first_with_sorted_letters_and_digits_in_original_order(self):
        self.input_list = ["let1 art can", "dig2 3 6", "dig1 8 1 5 1", "let2 own kit dig", "let3 art zero"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["let1 art can", "let3 art zero", "let2 own kit dig", "dig2 3 6", "dig1 8 1 5 1"])

    def test_letter_list_returns_lexicographic_order(self):
        self.input_list = ["let2 own kit dig", "let3 art zero", "let1 art can"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["let1 art can", "let3 art zero", "let2 own kit dig"])
        

    def test_letter_list_with_ties_returns_lexicographic_order_broken_by_identifier(self):
        self.input_list = ["let2 a b c", "let1 a b c", "let3 a b"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["let3 a b", "let1 a b c", "let2 a b c"])

    def test_other_identifiers_for_letters(self):
        self.input_list = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
        output_list = self.solution.reorderLogFiles(self.input_list)
        self.assertEquals(output_list, ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])