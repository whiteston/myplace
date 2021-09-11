"""
Find the nearest value to the given one.
You are given a list of values as set form and a value for which you need to find the nearest one.

For example, we have the following set of numbers: 4, 7, 10, 11, 12, 17, 
and we need to find the nearest value to the number 9.

If we sort this set in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10.
But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:

-If 2 numbers are at the same distance, you need to choose the smallest one;
-The set of numbers is always non-empty, i.e. the size is >=1;
-The given value can be in this set, which means that it’s the answer;
-The set can contain both positive and negative numbers, but they are always integers;
-The set isn’t sorted and consists of unique numbers.

Input: Two arguments. A list of values in the set form. The sought value is an int.
Output: Int.

Example:

nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
"""


def nearest_value(values: set, one: int) -> int:
    if one > 0:
        return min(values, key = lambda x: abs(x - one)) #values랑 key를 비교해서 최솟값을 찾을건데 key는 lambda~ 특성을 갖고 있다.
    else:
        return max(values, key = lambda x: (one - x))

print(nearest_value({0, -2}, -1))
print(nearest_value({4, 7, 10, 11, 12, 17}, 9)) 
print(nearest_value({4, 8, 10, 11, 12, 17}, 9))
print(nearest_value({5, 10, 8, 12, 89, 100}, 7))
print(nearest_value({-1, 2, 3}, 0))

# 식을 세우는데 어려움이 있어서 아래 사이트 참고했음.
# https://stackoverflow.com/questions/12141150/from-list-of-integers-get-number-closest-to-a-given-value
# lambda에 대해 더 공부해야겠다.