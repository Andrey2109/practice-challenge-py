"""You will be given a list of 32-bit unsigned integers. Flip all the bits ( 1->0 and 0->1) and return the result as an
unsigned integer."""
import unittest


def flippingBits(n):
    flipped = n ^ 0xFFFFFFFF  # XOR with all 1s (32-bit)
    return flipped


print(flippingBits(45890))


class TestFlippingBits(unittest.TestCase):

    def test_flipping_small_number(self):
        self.assertEqual(flippingBits(9), 4294967286)

    def test_flipping_large_number(self):
        self.assertEqual(flippingBits(4294967286), 9)

    def test_flipping_max_value(self):
        self.assertEqual(flippingBits(4294967295), 0)


# Running the tests
if __name__ == '__main__':
    unittest.main()