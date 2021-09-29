"""
In a given list the last element should become the first one.
An empty list or list with only one element should stay the same.

Input : List.
Output : Iterable.

Example:

replace_last([2, 3, 4, 1]) == [1, 2, 3, 4]
replace_last([1, 2, 3, 4]) == [4, 1, 2, 3]
replace_last([1]) == [1]
replace_last([]) == []
"""


def replace_last(line: list) -> list:
    if len(line) > 1:
        line.insert(0, line[-1])
        del line[-1]
    return line

print(replace_last([1]))