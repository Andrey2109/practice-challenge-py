"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element
in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
to reach the last index.

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""

import unittest


class Solution(object):
    def can_jump(self, nums):
        max_reachable = 0  # Tracks the farthest index you can reach
        for i, steps in enumerate(nums):
            if max_reachable < i:
                return False

            max_reachable = max(max_reachable, i + steps)

        return True


jumper = Solution()
print(jumper.can_jump([2, 3, 1, 1, 4]))  # This should output True


class TestCanJump(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reachable(self):
        self.assertTrue(self.solution.can_jump([2, 3, 1, 1, 4]), "Should return True when the last index is reachable")

    def test_not_reachable(self):
        self.assertFalse(self.solution.can_jump([3, 2, 1, 0, 4]),
                         "Should return False when the last index is not reachable")

    def test_single_element(self):
        self.assertTrue(self.solution.can_jump([0]), "Should return True when there is only one element")

    def test_all_zeros(self):
        self.assertFalse(self.solution.can_jump([0, 0, 0]),
                         "Should return False when the array contains all zeros except the first element")


if __name__ == '__main__':
    unittest.main()
