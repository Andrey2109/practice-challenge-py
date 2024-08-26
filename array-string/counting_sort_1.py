"""Comparison Sorting
Quicksort usually has a running time of n * log(n), but is there an algorithm that can sort
even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list
just by comparing the elements to one another. A comparison sort algorithm cannot beat n * log(n) (worst-case)
running time, since n * log(n) represents the minimum number of comparisons needed to know where to place each
element.
 Alternative Sorting
 Another sorting method, the counting sort, does not require comparison. Instead,
you create an integer array whose index range covers the entire range of values in your array to sort. Each time a
value occurs in the original array, you increment the counter at that index. At the end, run through your counting
array, printing the value of each non-zero valued index that number of times.

Challenge
Given a list of integers, count and return the number of times each value appears as an array of integers.

Function Description

Complete the countingSort function in the editor below.

countingSort has the following parameter(s):

arr[n]: an array of integers
Returns

int[100]: a frequency array"""
import unittest


def counting_sort(arr):
    sorted_arr = [0] * 100
    for i in arr:
        sorted_arr[i] += 1

    return sorted_arr


print((counting_sort(
    [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76,
     85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78,
     24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16,
     82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
    )))


class TestCountingSort(unittest.TestCase):

    def test_counting_sort_typical(self):
        arr = [63, 25, 73, 1, 98, 56, 84, 86, 57, 16]
        expected_output = [0] * 100
        expected_output[1] = 1
        expected_output[16] = 1
        expected_output[25] = 1
        expected_output[56] = 1
        expected_output[57] = 1
        expected_output[63] = 1
        expected_output[73] = 1
        expected_output[84] = 1
        expected_output[86] = 1
        expected_output[98] = 1

        self.assertEqual(counting_sort(arr), expected_output)

    def test_counting_sort_empty(self):
        arr = []
        expected_output = [0] * 100
        self.assertEqual(counting_sort(arr), expected_output)

    def test_counting_sort_repeated(self):
        arr = [1, 1, 1, 98, 98, 56]
        expected_output = [0] * 100
        expected_output[1] = 3
        expected_output[56] = 1
        expected_output[98] = 2

        self.assertEqual(counting_sort(arr), expected_output)


if __name__ == '__main__':
    unittest.main()