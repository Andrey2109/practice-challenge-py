"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Example
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.

Function Description

Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):

int a[n]: an array of integers
Returns

int: the element that occurs only once
Input Format

The first line contains a single integer, n, the number of integers in the array.
The second line contains n space-separated integers that describe the values in a.
"""
import unittest


def lonelyinteger(a):
    integer_count = {}
    for i in a:
        if i in integer_count:
            integer_count[i] += 1
        else:
            integer_count[i] = 1
    for k, v in integer_count.items():
        if v == 1:
            return k


class TestLonelyInteger(unittest.TestCase):

    def test_single_lonely_integer(self):
        a = [1, 2, 3, 2, 1]
        self.assertEqual(lonelyinteger(a), 3)

    def test_all_identical_except_one(self):
        a = [0, 0, 1, 1, 2]
        self.assertEqual(lonelyinteger(a), 2)

    def test_large_input(self):
        a = [4, 9, 95, 93, 57, 4, 57, 93, 9]
        self.assertEqual(lonelyinteger(a), 95)


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))

if __name__ == '__main__':
    unittest.main()