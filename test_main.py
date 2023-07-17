import unittest
from main import get_list_of_pairs_eq_target, print_pretty
import sys
from io import StringIO

class TestGetListOfPairsEqTarget(unittest.TestCase):

    def assertListIgnoreOrder(self, result, expected):
        for pair in expected:
            self.assertIn(pair, result)
        self.assertEqual(len(result), len(expected))

    def test_empty_list(self):
        result = get_list_of_pairs_eq_target([], 10)
        self.assertListIgnoreOrder(result, [])

    def test_no_pairs(self):
        result = get_list_of_pairs_eq_target([1, 2, 3, 4], 10)
        self.assertListIgnoreOrder(result, [])

    def test_single_pair(self):
        result = get_list_of_pairs_eq_target([1, 2, 3, 4, 5], 7)
        self.assertListIgnoreOrder(result, [[2, 5], [3,4]])

    def test_multiple_pairs(self):
        result = get_list_of_pairs_eq_target([1, 2, 3, 4, 5, 6, 7], 7)
        self.assertListIgnoreOrder(result, [[1, 6], [2, 5], [3, 4]])

    def test_repeated_target(self):
        result = get_list_of_pairs_eq_target([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        self.assertListIgnoreOrder(result, [[4, 6], [3, 7], [2, 8], [1, 9]])

    def test_negative_numbers(self):
        result = get_list_of_pairs_eq_target([-1, 2, -3, 4, -5], -1)
        self.assertListIgnoreOrder(result, [[2, -3], [4, -5]])

class TestPrintPretty(unittest.TestCase):
    def test_empty_list(self):
        list_of_pairs = []
        captured_output = StringIO()
        sys.stdout = captured_output

        print_pretty(list_of_pairs)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), '')

    def test_single_pair(self):
        list_of_pairs = [[2, 3]]
        captured_output = StringIO()
        sys.stdout = captured_output

        print_pretty(list_of_pairs)

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), '0. 2 + 3 = 5')

    def test_multiple_pairs(self):
        list_of_pairs = [[1, 2], [3, 4], [5, 6]]
        captured_output = StringIO()
        sys.stdout = captured_output

        print_pretty(list_of_pairs)

        sys.stdout = sys.__stdout__
        expected_output = """\
0. 1 + 2 = 3
1. 3 + 4 = 7
2. 5 + 6 = 11"""
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()
