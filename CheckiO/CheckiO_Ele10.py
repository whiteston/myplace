"""
Split the string into pairs of two characters.
If the string contains an odd number of characters, 
then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.
Output: An iterable of strings.

Example:

split_pairs('abcd') == ['ab', 'cd']
split_pairs('abc') == ['ab', 'c_']

Precondition: 0<=len(str)<=100
"""


def split_pairs(a):
    new = []

    if len(a) % 2 != 0: #문자 개수가 홀수일 때 짝수로 먼저 맞춰주고 뒤에 식 계산.
        a += '_'

    for i in range(0, len(a), 2):
        new.append(a[i: i + 2])
    return new


print(split_pairs('adcbe'))

# 조금 다른 형태로 나오지만 이런 방법도 가능

# def split_pairs(a):
#     if len(a) % 2 != 0:
#         a = a + '_'
#     return list(zip(a[0::2], a[1::2]))