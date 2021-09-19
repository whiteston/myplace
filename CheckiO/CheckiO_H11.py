"""
You are given a non-empty list of integers (X).
For this task, you should return a list consisting of only the non-unique elements in this list.
To do so you will need to remove all unique elements (elements which are contained in a given list only once).
When solving this task, do not change the order of the list. 


Input: A list of integers.
Output: An iterable of integers.

Example:

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3] -> 1 and 3 non-unique elements and result will be [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
checkio([2]) == []

Precondition:
0 < len(data) < 1000


"""


def checkio(data: list) -> list:
    a = []
    for x in data:
        if data.count(x) >= 2:
            a.append(x)
    return a
        

print(checkio([3, 2, 3, 1, 3]))
print(checkio([5, 4, 3, 2, 1]))
print(checkio([5, 5, 5]))
print(checkio([9, 10, 19, 98, 9, 10])) 
print(checkio([7, 5]))