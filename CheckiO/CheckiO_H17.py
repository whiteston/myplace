"""
You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. 
If it has no elements, then two empty arrays should be returned.

Input : Array.
Output : Array or two arrays.

Example:

split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
split_list([1, 2, 3]) == [[1, 2], [3]]
"""


def split_list(items: list) -> list:

    if len(items) % 2 == 0:
        return [items[0: len(items) // 2], items[len(items) // 2:]]
    return [items[: len(items) // 2 + 1], items[len(items) // 2 + 1:]]

# 도움이 된 새로운 아이디어
    # 결국 자릿수에 따라 0, 1 / 2, 3 / 4, 5 ... 짝,홀의 몫이 같은 걸 파악했는가. 이게 포인트인 듯.
    # return [items[: (len(items) + 1) // 2], items[(len(items) + 1) // 2:]]

print(split_list([1, 5, 3, 15, 5, 26, 9]))