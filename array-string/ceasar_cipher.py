"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b, and c.

Original alphabet: abcdefghijklmnopqrstuvwxyz

Alphabet rotated +3: defghijklmnopqrstuvwxyzabc

Example

S = There’s-a-starman-waiting-in-the-sky

K = 3

The alphabet is rotated by 3, matching the mapping above. The encrypted string is:

Wkhuh’v-d-vwdupdp-zdlwlqj-lq-wkh-vnb.

Note: The cipher only encrypts letters; symbols, such as '-', remain unencrypted.

Function Description

Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string
Input Format

The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.

Constraints

1 ≤ n ≤ 100
0 ≤ k ≤ 100

s is a valid ASCII string without any spaces.
"""
import unittest


def caesar_cipher(s, k):
    lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    k = k % 26

    result = []

    for c in s:
        if c.islower():
            new_char = lowercase_alphabet[(lowercase_alphabet.index(c) + k) % 26]
            result.append(new_char)
        elif c.isupper():
            new_char = uppercase_alphabet[(uppercase_alphabet.index(c) + k) % 26]
            result.append(new_char)
        else:

            result.append(c)

    return ''.join(result)


print(caesar_cipher("There's-a-starman-waiting-in-the-sky", 3))

class TestCaesarCipher(unittest.TestCase):

    def test_sample_case(self):
        self.assertEqual(caesar_cipher("middle-Outz", 2), "okffng-Qwvb")

    def test_no_rotation(self):
        self.assertEqual(caesar_cipher("hello-World", 0), "hello-World")



if __name__ == '__main__':
    unittest.main()