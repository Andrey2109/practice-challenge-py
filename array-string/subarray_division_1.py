import unittest

reportGeneralTypeIssues = False

"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

"""


def birthday(s, d, m):
    count = 0
    for i in range(len(s)):
        if sum(s[i:i + m]) == d:
            count += 1

    return count


result = birthday([2, 2, 1, 3, 2], 4, 2)
print(result)


class TestBirthday(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(birthday([2, 2, 1, 3, 2], 4, 2), 2)

    def test_no_valid_divisions(self):
        self.assertEqual(birthday([1, 1, 1, 1, 1], 3, 2), 0)

    def test_all_valid_divisions(self):
        self.assertEqual(birthday([4, 4, 4, 4], 4, 1), 4)


if __name__ == '__main__':
    unittest.main()