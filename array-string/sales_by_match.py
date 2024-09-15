"""There is a large pile of socks that must be paired by color. Given an array of integers representing the color of
each sock, determine how many pairs of socks with matching colors there are.

There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer , the number of socks represented in ar .
The second line contains  space-separated integers, ar[i], the colors of the socks in the pile.
"""
import unittest


def sock_merchant(n, ar):
    pairs = {}
    pairs_sum = 0
    for i in range(n):
        if ar[i] in pairs.keys():
            pairs[ar[i]] += 1
        else:
            pairs[ar[i]] = 1

    for key, value in pairs.items():
        pairs_sum += value // 2

    return pairs_sum


sock_merchant(7, [1, 2, 1, 2, 1, 3, 2])


class TestSockMerchant(unittest.TestCase):
    def test_normal_case(self):
        n = 7
        ar = [1, 2, 1, 2, 1, 3, 2]
        result = sock_merchant(n, ar)
        self.assertEqual(result, 2)

    def test_no_pairs(self):
        n = 5
        ar = [1, 2, 3, 4, 5]
        result = sock_merchant(n, ar)
        self.assertEqual(result, 0)

    def test_empty_list(self):

        n = 0
        ar = []
        result = sock_merchant(n, ar)
        self.assertEqual(result, 0)
