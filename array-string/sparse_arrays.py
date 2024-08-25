"""There is a collection of input strings and a collection of query strings. For each query string, determine how
many times it occurs in the list of input strings. Return an array of the results.


Function Description

Complete the function matchingStrings in the editor below. The function must return an array of integers representing
the frequency of occurrence of each query string in strings.

matchingStrings has the following parameters:

string strings[n] - an array of strings to search
string queries[q] - an array of query strings
Returns

int[q]: an array of results for each query
Input Format

The first line contains and integer n, the size of strings[].
Each of the next n lines contains a string strings[i] .
The next line contains q, the size of queries[].
Each of the next q lines contains a string queries[i].
"""
import unittest


def matchingStrings(strings, queries):
    res = []
    # counter = 0
    # for i in queries:
    #     for j in strings:
    #         if i == j:
    #             counter += 1
    #     res.append(counter)
    #     counter = 0
    string_counts = {}
    for s in strings:
        if s in string_counts:
            string_counts[s] += 1
        else:
            string_counts[s] = 1

    for q in queries:
        res.append(string_counts.get(q, 0))

    return res


class TestMatchingStrings(unittest.TestCase):

    def test_basic_case(self):
        strings = ["ab", "ab", "abc"]
        queries = ["ab", "abc", "bc"]
        expected = [2, 1, 0]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_no_matches(self):
        strings = ["a", "b", "c"]
        queries = ["x", "y", "z"]
        expected = [0, 0, 0]
        self.assertEqual(matchingStrings(strings, queries), expected)

    def test_all_queries_match(self):
        strings = ["cat", "dog", "cat", "dog", "cat"]
        queries = ["cat", "dog"]
        expected = [3, 2]
        self.assertEqual(matchingStrings(strings, queries), expected)


# Running the tests
if __name__ == '__main__':
    unittest.main()

print(matchingStrings(["ab", "ab", "abc"], ['ab', 'abc', 'bc']))
