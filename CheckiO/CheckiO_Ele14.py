"""
For the input of your function, you will be given one sentence.
You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Pay attention to the fact that not all of the fixes are necessary.
If a sentence already ends with a period (dot), then adding another one will be a mistake.

Input: A string.
Output: A string.

Example:

correct_sentence("greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends") == "Greetings, friends."
correct_sentence("Greetings, friends.") == "Greetings, friends."

Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .
"""


def correct_sentence(text: str) -> str:
#    if text[-1] != '.':                         -> 처음에 이렇게 작성했는데 만약 문장 끝에 '.'이 2개 오면 제대로 출력을 못함.
#        return text[0].upper() + text[1:] + '.'
#        
#    return text[0].upper() + text[1:]

    return ("{}{}.".format(text[0].upper(), text[1:].rstrip('.'))) 
    # format 함수를 사용해서 나타낼 수 있음. {}{} 차례대로 입력, 오른쪽 '.'을 모두 지우고 하나만 남기는 방법.

print(correct_sentence("greetings, friends"))
print(correct_sentence("hi, my name is Peter"))
print(correct_sentence("welcome to New York"))
print(correct_sentence("Greetings, friends.."))