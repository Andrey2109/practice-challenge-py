"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

Given an array of n distinct integers, transform the array into a zigzag sequence by permuting the array elements. A
sequence will be called a zigzag sequence if the first k elements in the sequence are in increasing order and the
last k elements are in decreasing order, where k = (n + 1)/2. You need to find the lexicographically smallest zigzag sequence of
the given array.

Example.

a=[2,3,5,1,4]

Now if we permute the array as

[1,4,5,3,2] the result is a zigzag sequence.

Debug the given function findZigZagSequence to return the appropriate zigzag sequence for the given input array.

Note: You can modify at most three lines in the given code. You cannot add or remove lines of code.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The first line contains t the number of test cases. The first line of each test case contains an integer n,
denoting the number of array elements. The next line of the test case contains n elements of array a. """


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n-1)//2)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


findZigZagSequence([2, 3, 5, 1, 4, 6, 7], 7)


test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)