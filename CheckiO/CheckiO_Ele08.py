"""
In a given list the first element should become the last one. 
An empty list or list with only one element should stay the same.

Input: List.
Output: Iterable.

Example:

replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
replace_first([1]) == [1]
"""


from typing import Iterable

def replace_first(items:list) -> Iterable:  
    if len(items) > 0:
        f_list = []
        for i in items[:1]:
            f_list.append(i)

        return items[1:] + f_list
    
    else:
        return items

    #return items[1:] + items[0:1] -> 슬라이싱으로 쉽게 해결 가능.
    #replace_first=lambda items:items[1:]+items[0:1] -> 함수 대신 lambda를 사용해서 표현할 수 있다.

print(replace_first([1, 3, 5, 7, 9]))
print(replace_first([]))
