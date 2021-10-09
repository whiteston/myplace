"""
A median is a numerical value separating the upper half of a sorted array of numbers from the lower half.
In a list where there are an odd number of entities, the median is the number found in the middle of the array.

If the array contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle.

For this mission, you are given a non-empty array of natural numbers (X).
With it, you must separate the upper half of the numbers from the lower half and find the median.

Input: An array as a list of integers.
Output: The median as a float or an integer.

Example:

checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5

Precondition: 
1 < len(data) ≤ 1000
all(0 ≤ x < 10 ** 6 for x in data)
"""

from typing import List

def checkio(data: List[int]):
    data.sort()

    if len(data) % 2 != 0:
        return data[(len(data) - 1) // 2]
    
    return (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2

print(checkio([3, 6, 20, 99, 10, 15]))