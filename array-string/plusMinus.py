"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the
decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers
with absolute error of up to 10^-4 are acceptable.
"""
import sys
import unittest
from io import StringIO


def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0
    for i in arr:
        if i > 0:
            positive += 1

        elif i < 0:
            negative += 1

        else:
            zeros += 1

    print(f"{positive / len(arr):.6f}")
    print(f"{negative / len(arr):.6f}")
    print(f"{zeros / len(arr):.6f}")


plusMinus([1, 1, 0, -1, -1])


class TestPlusMinus(unittest.TestCase):

    def test_mixed_values(self):
        arr = [1, -2, 0, 3, -4]
        expected_output = "0.400000\n0.400000\n0.200000\n"
        self.assert_function_output(plusMinus, arr, expected_output)

    def test_all_positive(self):
        arr = [1, 2, 3, 4, 5]
        expected_output = "1.000000\n0.000000\n0.000000\n"
        self.assert_function_output(plusMinus, arr, expected_output)

    def test_all_zeroes(self):
        arr = [0, 0, 0]
        expected_output = "0.000000\n0.000000\n1.000000\n"
        self.assert_function_output(plusMinus, arr, expected_output)

    def assert_function_output(self, func, args, expected_output):
        captured_output = StringIO()
        original_stdout = sys.stdout
        try:
            sys.stdout = captured_output
            func(args)
            output = captured_output.getvalue()
        finally:
            sys.stdout = original_stdout  # Ensure stdout is reset
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
