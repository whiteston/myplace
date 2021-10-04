"""
The first mission is quite simple. There is a light bulb, which by default is off, and a button, by pressing which the light bulb switches its state. 
This means that if the light bulb is off and the button is pressed, the light turns on, and if you press it again, it turns off.

The function input is an array of datetime objects - this is the date and time of pressing the button. 
Your task is to determine how long the light bulb has been turned on.

Input : A list of datetime objects
Output : A number of seconds as an integer.

Example:

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
]) == 610

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 10 , 10),
    datetime(2015, 1, 12, 11, 0 , 0),
    datetime(2015, 1, 12, 11, 10 , 10),
]) == 1220

sum_light([
    datetime(2015, 1, 12, 10, 0 , 0),
    datetime(2015, 1, 12, 10, 0 , 1),
]) == 1

Precondition:

The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements (which means the result should always be bigger than 0)
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""


from datetime import datetime
from typing import List

def sum_light(els: List[datetime]) -> int:
    light = []
    for i in range(1, len(els) + 1, 2):
        light_1 = ((els[i] -els[i - 1]).days) * 24 * 60 * 60
        light_2 = (els[i] -els[i - 1]).seconds
        light.append(light_1)
        light.append(light_2)
    return sum(light)

# 도움이 된 새로운 아이디어
    # return sum(int((check - els[els.index(check)-1]).total_seconds()) for check in els[1::2])
        ## total_seconds() : Return the total number of seconds contained in the duration.

# from datetime import timedelta 추가하고 아래처럼 표현 가능. 
    # return sum(timedelta.total_seconds(els[counts + 1] - els[counts]) for counts in range(0, len(els) - 1, 2))

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 13, 11, 0, 0)
]))