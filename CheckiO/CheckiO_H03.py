"""
You are given a string with words and numbers separated by whitespaces (one space).
The words contains only letters. You should check if the string contains three words in succession.
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.

Example:

checkio("Hello World hello") == True
checkio("He is 123 man") == False
checkio("1 2 3 4") == False
checkio("bla bla bla bla") == True
checkio("Hi") == False

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
"""


def checkio(words: str) -> bool:
    list = words.split()
    one = 0
    end = False

    for i in list:
        if i.isalpha():
            one += 1
            if one >2:
                end = True
        else:
            one = 0
    return end


print(checkio("Today is my 26th birthday!"))
print(checkio("3 2 1 Game Over"))
print(checkio("Bye"))