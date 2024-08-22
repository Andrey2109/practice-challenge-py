"""Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four
of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated
long integers.
 Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of 5 integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of 4 of 5 elements.

Input Format

A single line of five space-separated integers.

"""
import unittest


def mini_max_sum(arr):
    arr = sorted(arr)
    sum_min = sum(arr[:-1])
    sum_max = sum(arr[1:])
    print(sum_min, sum_max)

    return sum_min, sum_max


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]
    mini_max_sum(arr)

class TestMiniMaxSum(unittest.TestCase):
    def test_case_1(self):
        arr = [1, 2, 3, 4, 5]
        result = mini_max_sum(arr)
        self.assertEqual(result, (10, 14))  # Expected output: 10 14

    def test_case_2(self):
        arr = [7, 69, 2, 221, 8974]
        result = mini_max_sum(arr)
        self.assertEqual(result, (299, 9271))  # Expected output: 299 9271

    def test_case_3(self):
        arr = [5, 5, 5, 5, 5]
        result = mini_max_sum(arr)
        self.assertEqual(result, (20, 20))  # Expected output: 20 20

# Running the tests
if __name__ == '__main__':
    unittest.main(argv=[''])