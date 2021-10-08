"""
Not all of the elements are important. What you need to do here is to remove all of the elements after the given one from list.
For illustration, we have an list [1, 2, 3, 4, 5] and we need to remove all the elements that go after 3 - which is 4 and 5.

We have two edge cases here: 
(1) if a cutting element cannot be found, then the list shouldn't be changed; 
(2) if the list is empty, then it should remain empty.

Input: List and the border element.
Output: Iterable (tuple, list, iterator ...).

Example:

remove_all_after([1, 2, 3, 4, 5], 3) == [1, 2, 3]
remove_all_after([1, 1, 2, 2, 3, 3], 2) == [1, 1, 2]
"""


from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    try:
        return items[:items.index(border) + 1]
    except ValueError:
        return items

print(remove_all_after([1, 2, 3, 4, 5], 4))
print(remove_all_after([1, 1, 3, 3, 4, 5], 3))