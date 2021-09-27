"""
In this mission you should check if all elements in the given list are equal.

Input : List.
Output : Bool.

Example:

all_the_same([1, 1, 1]) == True
all_the_same([1, 2, 1]) == False
all_the_same(['a', 'a', 'a']) == True
all_the_same([]) == True

Precondition: all elements of the input list are hashable
"""


from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # elements == [] 대신 not elements도 가능.
    if elements == [] or elements.count(elements[0]) == len(elements):
        return True
    return False

# return True if len(set(elements)) in [0,1] else False
  # set를 사용하면 중복된 문자형 모두 하나로 인식하니까 set(elements)의 개수(len)를 세어서 0 또는 1이면 True 반환!
print(all_the_same([1, 2, 3]))
print(all_the_same(['v', 'v', 'v']))
