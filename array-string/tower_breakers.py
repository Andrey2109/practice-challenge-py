"""Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play
optimally. The rules of the game are as follows:

- Initially there are n towers. - Each tower is of height m. - The players move in alternating turns. - In each turn,
a player can choose a tower of height x and reduce its height to y, where 1 ≤ y < x and y evenly divides x. - If the
current player is unable to make a move, they lose the game.

Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

Example, n = 2, m = 6

There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:

- remove 3 pieces from a tower to leave 3 as 6 modulo 3 = 0
- remove 5 pieces to leave 1

Let Player 1 remove 3. Now the towers are 3 and 6 units tall. Player 2 matches the move. Now the towers are both 3
units tall. Now Player 1 has only one move. Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
Player 2 matches again. Towers are both 1 unit tall. Player 1 has no move and loses. Return 2.

Function Description

Complete the towerBreakers function in the editor below.

towerBreakers has the following parameter(s):
- int n: the number of towers
- int m: the height of each tower

Returns:
- int: the winner of the game

Input Format

The first line contains a single integer t, the number of test cases.
Each of the next t lines describes a test case in the form of 2 space-separated integers, n and m.

Constraints

- 1 ≤ t ≤ 100
- 1 ≤ n, m ≤ 10^6

"""
import unittest


def tower_breakers(n, m):
    if m == 1:
        return 2

    return 1 if n % 2 == 1 else 2


print(tower_breakers(2, 6))


class TestTowerBreakers(unittest.TestCase):
    def test_normal_case(self):
        n = 2
        m = 6
        result = tower_breakers(n, m)
        self.assertEqual(result, 2)

    def test_odd_number_of_towers(self):
        n = 3
        m = 6
        result = tower_breakers(n, m)
        self.assertEqual(result, 1, "Expected Player 1 to win with odd number of towers and height > 1")

    def test_single_height_towers(self):
        n = 5
        m = 1
        result = tower_breakers(n, m)
        self.assertEqual(result, 2, "Expected Player 2 to win with towers of height 1, regardless of number")


if __name__=="__main__":

    unittest.main()