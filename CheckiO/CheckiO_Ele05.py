"""
You should return a given string in reverse order.

Input: A string.
Output: A string.

Example:

backward_string('val') == 'lav'
backward_string('') == ''
backward_string('ohho') == 'ohho'
backward_string('123456789') == '987654321'
"""


def backward_string(name: str):
    return ''.join(reversed(name))

print(backward_string('var'))
print(backward_string('1988_seoul'))
print()

# 리스트 슬라이싱으로도 뒤집기 가능함.
def back_string(new: str):
    return new[::-1]

print(back_string('hola'))