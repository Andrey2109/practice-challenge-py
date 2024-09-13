"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
Debug the given function strings_xor to find the XOR of the two given strings appropriately.

Note: You can modify at most three lines in the given code and you cannot add or remove lines to the code.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The input consists of two lines. The first line of the input contains the first string, s, and the second line
contains the second string, t . """
import unittest


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res


strings_xor('10101', '00101')


class TestStringXor(unittest.TestCase):
    def test_usual_case(self):
        s = '10101'
        t = '00101'
        expected_res = '10000'
        result = strings_xor(s, t)
        self.assertEqual(result, expected_res)

    def test_all_matching_bits(self):
        s = '11111'
        t = '11111'
        expected_res = '00000'
        result = strings_xor(s, t)
        self.assertEqual(result, expected_res)

    def test_all_different_bits(self):
        s = '11111'
        t = '00000'
        expected_res = '11111'
        result = strings_xor(s, t)
        self.assertEqual(result, expected_res)


if __name__ == "__main__":
    unittest.main()
