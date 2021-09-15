"""
In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string.
Output: An int.

Example:

sum_numbers('hi') == 0
sum_numbers('who is 1st here') == 0
sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
sum_numbers('5 plus 6 is') == 11
sum_numbers('') == 0
"""


def sum_numbers(text: str) -> int:
    k = []

    for x in range(len(text.split())):
        if text.split()[x].isdigit() == True:
            k.append(int(text.split()[x]))
        else:
            continue
    return sum(k)

# return sum([int(i) for i in text.split() if i.isdigit()]) 
#  -24~25번째 줄을 합쳐서 for i in text.split() 이렇게 나타내고 if i.isdigit() 조건 걸기
#  -출력된 값을 22, 26번째 줄 대신 [] 안에 식을 넣고, 29 = 마지막에 정수로 변환해서 sum해주면 된다.

print(sum_numbers('hi 234 789 man'))
print(sum_numbers('who is 2st here'))
print(sum_numbers('iphone 13 applewatch 7'))
print(sum_numbers('80 plus 13 is'))