"""
There are two n-element arrays of integers, A and B. Permute them into some A' and B'
such that the relation A'[i] + B'[i] ≥ k holds for all i where 0 ≤ i < n.

There will be q queries consisting of A, B, and k. For each query, return YES if some
permutation A', B' satisfying the relation exists. Otherwise, return NO.

Example:
    A = [0, 1]
    B = [0, 2]
    k = 1

    A valid A', B' is A' = [1, 0] and B' = [0, 2]: 1 + 0 ≥ 1 and 0 + 2 ≥ 1.
    Return YES.

Function Description:
    Complete the twoArrays function in the editor below. It should return a string,
    either YES or NO.

    twoArrays has the following parameter(s):
        int k: an integer
        int A[n]: an array of integers
        int B[n]: an array of integers

    Returns:
        string: either YES or NO
"""
import unittest


def two_arrays(k, A, B):
    A.sort()  # Sort A in ascending order
    B.sort(reverse=True)  # Sort B in descending order

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"

    return "YES"


class TestTwoArrays(unittest.TestCase):

    def test_case_1(self):
        A = [0, 1]
        B = [0, 2]
        k = 1
        result = two_arrays(k, A, B)
        self.assertEqual(result, "YES")

    def test_case_2(self):
        A = [1, 2, 3]
        B = [7, 8, 9]
        k = 10
        result = two_arrays(k, A, B)
        self.assertEqual(result, "YES")

    def test_case_3(self):
        A = [1, 2, 2, 1]
        B = [3, 3, 3, 4]
        k = 6
        result = two_arrays(k, A, B)
        self.assertEqual(result, "NO")


if __name__ == '__main__':
    unittest.main()


print(two_arrays(10, [2, 1, 3], [7, 8, 9]))
