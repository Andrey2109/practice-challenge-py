"""Given an array of integers citations where citations[i] is the number of citations a researcher received for their
ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the
given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5] Output: 3 Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3
citations each and the remaining two with no more than 3 citations each, their h-index is 3. Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""


class Solution:
    def hIndex(self, citations):
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0

solution = Solution()
print(solution.hIndex([1, 3, 3, 1, 1]))

import unittest

class TestHIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_h_index_standard_case(self):
        # Standard case with mixed citation counts
        citations = [3, 0, 6, 1, 5]
        expected_h_index = 3
        self.assertEqual(self.solution.hIndex(citations), expected_h_index)

    def test_h_index_all_zero_citations(self):
        # All papers have zero citations
        citations = [0, 0, 0, 0]
        expected_h_index = 0
        self.assertEqual(self.solution.hIndex(citations), expected_h_index)

    def test_h_index_high_citations(self):
        # All papers have high citation counts
        citations = [10, 10, 10, 10, 10]
        expected_h_index = 5
        self.assertEqual(self.solution.hIndex(citations), expected_h_index)

if __name__ == '__main__':
    unittest.main()
