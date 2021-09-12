"""
You are given a string and two markers (the initial one and final). 
You have to find a substring enclosed between these two markers. But there are a few important conditions.

-The initial and final markers are always different.
-The initial and final markers are always 1 char size.
-The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.

Example:

between_markers('What is >apple<', '>', '<') == 'apple'

How it is used: For text parsing.

Precondition: There can't be more than one final and one initial markers.
"""

def between_markers(text: str, begin: str, end: str) -> str:
    i, j = text.find(begin), text.find(end)
    return text[i + 1: j]

print(between_markers('What is >apple<', '>', '<'))
print(between_markers("Manner maketh *Man_", "*", "_"))
