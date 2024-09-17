"""A teacher asks the class to open their books to a page number. A student can either start turning pages from the
front of the book or from the back of the book. They always turn pages one at a time. When they open the book,
page 1 is always on the right side:
When they flip page 1, they see pages 2 and 3. Each page except the last page will
always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the
book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn? They can
start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.

Example
The book has a total of 5 pages, numbered as n = 5.
A student wants to turn to page 3, denoted as p = 3.
Using the provided diagram:

If the student opens the book starting at page 1, they flip once and reach pages 2 and 3, landing on the correct page with just one flip.
If they open the book from the back starting at page 5, they also flip once backward to reach pages 3 and 4, making one flip to get to the correct page.
In both scenarios, the minimum number of pages turned is 1.

Function Description
The function named pageCount should be completed to determine the minimum number of page turns needed to reach a specified page from either the start or the end of the book.

Parameters:

int n: the number of pages in the book.
int p: the page number the user wishes to turn to.
Returns:

int: the minimum number of pages to turn.
Input Format
The first line contains an integer, n, the total number of pages in the book.
The second line contains an integer, p, the specific page number to reach.
Constraints
1 ≤ n ≤ 10^5
1 ≤ p ≤ n
"""
import unittest


def page_count(n, p):
    from_start_point = 1
    from_end_point = n
    num_to_turn_from_start = 0
    num_to_turn_from_end = 0
    while from_start_point < p:
        num_to_turn_from_start += 1
        from_start_point += 2
    while from_end_point > p:
        num_to_turn_from_end += 1
        from_end_point -= 2

    return min(num_to_turn_from_start, num_to_turn_from_end)


print(page_count(5, 5))

# more efficient solution:
# def page_count(n, p):
#     # Calculate turns from the start
#     turns_from_start = p // 2
#
#     # Calculate turns from the end
#     turns_from_end = (n // 2) - (p // 2)
#
#     # Return the minimum of the two
#     return min(turns_from_start, turns_from_end)


class TestPageCount(unittest.TestCase):
    def test_usual_case(self):
        n = 5
        p = 3
        result = page_count(n, p)
        expected_result = 1
        self.assertEqual(result, expected_result)

    def test_first_page(self):
        n = 20
        p = 1
        result = page_count(n, p)
        expected_result = 0
        self.assertEqual(result, expected_result)

    def test_last_page(self):
        n = 30
        p = 30
        result = page_count(n, p)
        expected_result = 0
        self.assertEqual(result, expected_result)