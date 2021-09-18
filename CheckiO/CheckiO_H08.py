"""
In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

Example:

backward_string_by_word('') == ''
backward_string_by_word('world') == 'dlrow'
backward_string_by_word('hello world') == 'olleh dlrow'
backward_string_by_word('hello   world') == 'olleh   dlrow'

Precondition: The line consists only from alphabetical symbols and spaces.
"""


# def backward_string_by_word(text: str) -> str:
#     for i in text.split():
#         text = text.replace(i, i[::-1])
#     return text

# 이렇게 생각했었는데 "olleH Hello"를 입력하면 "olleH olleH"로 반례가 생긴다.

def backward_string_by_word(text: str) -> str:
    texts = text.split(" ")
    newtext = [text[::-1] for text in texts]
    new = " ".join(newtext)

    return new

print(backward_string_by_word('hello   world'))