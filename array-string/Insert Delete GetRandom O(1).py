"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.



Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:

-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
"""
import random
import unittest


class RandomizedSet:

    def __init__(self):
        # Store the index of each val in self.arr.
        self.indices = {}
        # Store all vals.
        self.arr = []

    def insert(self, val: int) -> bool:
        # Return False if val is already present as requested.
        if val in self.indices: return False

        # Append val to the array.
        # Store its index in the hashmap
        self.arr.append(val)
        self.indices[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices: return False

        i = self.indices[val]

        self.indices[self.arr[-1]] = i

        self.arr[i] = self.arr[-1]

        self.indices.pop(val)
        self.arr.pop()

        return True

    def get_random(self) -> int:
        return random.choice(self.arr)


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.insert(2))
print(randomizedSet.insert(3))
print(randomizedSet.remove(1))
print(randomizedSet.get_random())


class TestRandomizedSet(unittest.TestCase):

    def test_insert(self):
        rset = RandomizedSet()
        self.assertTrue(rset.insert(1))  # Insert a new element, should return True
        self.assertFalse(rset.insert(1))  # Insert the same element, should return False
        self.assertTrue(rset.insert(2))  # Insert another new element, should return True

    def test_remove(self):
        rset = RandomizedSet()
        rset.insert(1)
        rset.insert(2)
        self.assertTrue(rset.remove(1))  # Remove an existing element, should return True
        self.assertFalse(rset.remove(1))  # Try to remove the same element again, should return False
        self.assertFalse(rset.remove(3))  # Try to remove a non-existing element, should return False

    def test_get_random(self):
        rset = RandomizedSet()
        rset.insert(1)
        rset.insert(2)
        rset.insert(3)
        result = rset.get_random()
        self.assertIn(result, [1, 2, 3])  # The result should be one of the inserted values

if __name__ == '__main__':
    unittest.main()