"""
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: 
-the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" 
then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.

Input: The text and the search words array.
Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

Example:

popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
    'i': 4,
    'was': 3,
    'three': 0,
    'near': 0
}

Precondition : The input text will consists of English letters in uppercase and lowercase and whitespaces.
"""


def popular_words(text: str, words: list) -> dict:
    l_text = text.lower().split()
# 찾고자 하는 문자는 소문자로 주어지기 때문에 text 문자열을 소문자로 바꾸는 작업 필요.
# split 함수로 공백으로 구분.    
    return {word : l_text.count(word) for word in words}
# 딕셔너리 {키:값} 순서대로 넣으면 출력 가능.     
        
print(popular_words('''
Cos ah ah I'm in the stars tonight
So watch me bring the fire
and set the night alight
Shining through the city
with a little funk and soul
So I'mma light it up like dynamite, woah
''', ['i', 'and', 'so', 'the']))