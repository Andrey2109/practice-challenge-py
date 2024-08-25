"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9
The left-to-right diagonal =15 . The right to left diagonal = 17. Their absolute difference is 2.
"""
import unittest


def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                left_to_right += arr[i][j]

    for i in range(len(arr) - 1, -1, -1):
        for j in range(len(arr[i]) - 1, -1, -1):
            if len(arr)-1 - i == j:
                right_to_left += arr[i][j]

    print(left_to_right, right_to_left)
    return abs(left_to_right - right_to_left)


diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]])


class TestDiagonalDifference(unittest.TestCase):

    def test_small_matrix(self):
        # Test with a 3x3 matrix
        arr = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(diagonalDifference(arr), 0)

    def test_larger_matrix(self):
        # Test with a 4x4 matrix
        arr = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        self.assertEqual(diagonalDifference(arr), 0)

    def test_matrix_with_different_diagonal_sums(self):
        # Test with a matrix where diagonals have different sums
        arr = [
            [6, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(diagonalDifference(arr), 5)


# Running the tests
if __name__ == '__main__':
    unittest.main()