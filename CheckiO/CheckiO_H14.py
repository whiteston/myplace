"""
Sort the given iterable so that its elements end up in the decreasing frequency order,
that is, the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable

Example:

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']

Precondition: elements can be ints or strings
"""


def frequency_sort(items):
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
    # lambda 함수를 사용해서 나타낼 수 있다. 값을 count해서 내림차순으로 정렬
    # 값의 개수가 같다면 index 기준으로 오름차순 정렬
    
print(frequency_sort([6, 4, 2, 6, 4, 4, 4, 2]))
print(frequency_sort(['un', 'bts', 'army', 'bts', 'un', 'un', 'army', 'bts']))