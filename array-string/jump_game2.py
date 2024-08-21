"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at
nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated
such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
it's guaranteed that you can reach nums[n - 1].
"""

import unittest


class Solution(object):
    def jump(self, nums):
        max_reachable = 0
        min_jumps = 0
        current_end = 0
        for i in range(len(nums)-1):
            max_reachable = max(max_reachable, i + nums[i])

            if current_end == i:
                min_jumps += 1
                current_end = max_reachable

                if current_end >= len(nums)-1:
                    return min_jumps

        return min_jumps




s = Solution()
print(s.jump([2, 3, 1, 1, 4]))


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_minimal_case(self):
        self.assertEqual(self.s.jump([0]), 0)

    def test_simple_case_one_jump(self):
        self.assertEqual(self.s.jump([1, 2]), 1)

    def test_two_jumps(self):
        self.assertEqual(self.s.jump([2, 3, 1, 1, 4]), 2)

    def test_already_at_last_index(self):
        self.assertEqual(self.s.jump([1]), 0)

    def test_no_need_to_jump(self):
        self.assertEqual(self.s.jump([10, 1, 1, 1, 1]), 1)

    def test_multiple_valid_paths(self):
        self.assertEqual(self.s.jump([2, 3, 0, 1, 4]), 2)


if __name__ == '__main__':
    unittest.main()
