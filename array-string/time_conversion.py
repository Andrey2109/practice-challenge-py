"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time
in 24-hour format.

timeConversion has the following parameter(s):

string s: a time in 12-hour format
Returns

string: the time in 24-hour format
Input Format

A single string  that represents a time in 12-hour clock format
"""
import unittest


def time_conversion(s):
    if s[-2:] == "AM" and int(s[:2]) < 12:
        print(s[:-2])
        return s[:-2]

    elif s[-2:] == "AM" and int(s[:2]) == 12:
        print("00" + s[2:-2])
        return "00" + s[2:-2]

    elif s[-2:] == "PM" and int(s[:2]) < 12:
        print(str(int(s[:2]) + 12) + s[2:-2])
        return str(int(s[:2]) + 12) + s[2:-2]

    elif s[-2:] == "PM" and int(s[:2]) == 12:
        print(s[:-2])
        return s[:-2]


time_conversion('08:05:45PM')


class TestTimeConversion(unittest.TestCase):
    def test_case_1(self):
        result = time_conversion('07:45:54PM')
        self.assertEqual(result, '19:45:54')  # Expected output: 19:45:54

    def test_case_2(self):
        result = time_conversion('12:00:00AM')
        self.assertEqual(result, '00:00:00')  # Expected output: 00:00:00

    def test_case_3(self):
        result = time_conversion('12:00:00PM')
        self.assertEqual(result, '12:00:00')  # Expected output: 12:00:00


if __name__ == "__main__":
    unittest.main()
