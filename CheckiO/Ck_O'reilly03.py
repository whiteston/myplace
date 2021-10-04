"""
You are given an array with positive numbers and a number N. 
You should find the N-th power of the element in the array with the index N. 
If N is outside of the array, then return -1. Don't forget that the first element has the index 0.

Input: Two arguments. An array as a list of integers and a number as a integer.
Output: The result as an integer.

Example:

index_power([1, 2, 3, 4], 2) == 9
index_power([1, 3, 10, 100], 3) == 1000000
index_power([0, 1], 0) == 1
index_power([1, 2], 3) == -1

Precondition: 0 < len(array) ≤ 10
0 ≤ N
all(0 ≤ x ≤ 100 for x in array)
"""


def index_power(array: list, n: int) -> int:
    if len(array) <= n:
        return -1
    return array[n] ** n

print(index_power([1, 3, 5, 7], 3))
print(index_power([1, 10, 77, 321], 2))
print(index_power([4, 1], 0))
print(index_power([1, 2], 3))