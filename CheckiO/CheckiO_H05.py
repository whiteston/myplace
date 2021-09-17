'''
You are given a string where you have to find its first word.
When solving a task pay attention to the following points:

-There can be dots and commas in a string.
-A string can start with a letter or, for example, a dot or space.
-A word can contain an apostrophe and it's a part of a word.
-The whole text can be represented with one word and that's it.

Input: A string.
Output: A string.

Example:

first_word("Hello world") == "Hello"
first_word("greetings, friends") == "greetings"

Precondition: the text can contain a-z A-Z , . '
'''


def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip() # replace를 반복해서 사용할 수 있다.
    text = text.split()
    
    return text[0]

print(first_word("  .Hello!, Python"))
