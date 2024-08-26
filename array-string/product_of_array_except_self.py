"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
import unittest


class Solution(object):
    def product_except_self(self, nums):
        n = len(nums)
        answer = [1] * n

        # Left pass: calculate the product of all elements to the left of each element
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]

        # Right pass: calculate the product of all elements to the right of each element
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


solution = Solution()
print(solution.product_except_self([1, 2, 3, 4]))


class TestProductExceptSelf(unittest.TestCase):

    def test_example_case_1(self):
        test_solution = Solution()
        result = test_solution.product_except_self([1, 2, 3, 4])
        expected = [24, 12, 8, 6]
        self.assertEqual(result, expected)

    def test_example_case_2(self):
        test_solution = Solution()
        result = test_solution.product_except_self([-1, 1, 0, -3, 3])
        expected = [0, 0, 9, 0, 0]
        self.assertEqual(result, expected)

    def test_all_ones(self):
        test_solution = Solution()
        result = test_solution.product_except_self([1, 1, 1, 1])
        expected = [1, 1, 1, 1]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
