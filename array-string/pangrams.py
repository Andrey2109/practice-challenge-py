"""A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a
pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
 Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a
pangram. Otherwise, it should return not pangram. """

import re
import unittest


def pangrams(s):
    pangram_s = re.findall("[a-z]", s.lower())
    if len(set(pangram_s)) == 26:
        return 'pangram'
    else:
        return 'not pangram'


print(pangrams("We promptly judged antique ivory buckles for the prize"))


class TestIsPangram(unittest.TestCase):

    def test_pangram(self):
        s = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(pangrams(s), 'pangram')

    def test_not_pangram(self):
        s = "Hello World"
        self.assertEqual(pangrams(s), 'not pangram')

    def test_pangram_with_extra_characters(self):
        s = "The quick brown fox jumps over the lazy dog! 1234567890."
        self.assertEqual(pangrams(s), 'pangram')


if __name__ == '__main__':
    unittest.main()
