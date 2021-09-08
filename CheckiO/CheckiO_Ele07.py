"""
Check if a given string has all symbols in upper case. 
If the string is empty or doesn't have any letter in it - function should return True.

Input: A string.
Output: a boolean.

Example:

is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('HeLlO PytHoN') == False
is_all_upper('') == True
is_all_upper('444') == True

"""


def is_all_upper(text):
    for i in text:
        if i.islower():
            return False
    return True

    # return text.upper() == text -> 한 줄로 간단하게 풀 수 있음.
    # return all([not(e.islower()) for e in text]) -> for 반복문 활용

print(is_all_upper('ALL UPPER'))
print(is_all_upper('all lower'))
print(is_all_upper('HeLlO PytHoN'))
print(is_all_upper(''))
print(is_all_upper('444'))
print(is_all_upper('     '))
print(is_all_upper('55 55 5'))