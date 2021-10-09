"""
This is the second mission in the lightbulb series. I will try to make each following task slightly more complex.
You have already learned how to count the amount of time a light bulb has been on, or how long a room has been lit. 
Now let's add one more parameter - the counting start time.
This means that the light continues to turn on and off as before. 
But now, as a result of the function, I want not only to know how long there was light in the room, but how long the room was lit, starting from a certain moment.
One more argument is added – start_watching , and if it’s not passed, we count as in the previous version of the program for the entire period.

Input : Two arguments and only the first one is required. The first one is a list of datetime objects and the second one is a datetime object.
Output: A number of seconds as an integer.

Example:

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
],
datetime(2015, 1, 12, 10, 0, 5)) == 5

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 0, 10),
], datetime(2015, 1, 12, 10, 0, 0)) == 10

sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
], datetime(2015, 1, 12, 11, 0, 0)) == 610

Precondition:

The array of pressing the button is always sorted in ascending order
The array of pressing the button has no repeated elements
The amount of elements is always even (the light will eventually be off)
The minimum possible date is 1970-01-01
The maximum possible date is 9999-12-31
"""


## 끝까지 풀지 못했던 문제
# 이 사이트를 참고해서 문제를 해결했다. 
# https://blog.csdn.net/weixin_44460564/article/details/114527190

from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    ## 1.

    #return sum(
    #    (
    #        max(start_watching or end, end) - max(start_watching or start, start)).total_seconds()
    #    for start, end in zip(els[::2], els[1::2])
    #    )

    ## 2.
    els = sorted(els + [start_watching]) # start_watching은 [] 를 사용해서 앞의 식에 추가할 수 있다.
    i = els.index(start_watching) # 그리고 els에서 start_watching 인덱스 값을 구한다.
    return sum([(els[j + 1] - els[j]). total_seconds() for j in range(i + (i % 2 == 0), len(els), 2)])

print(sum_light([
    datetime(2015, 1, 12, 10, 0, 0),
    datetime(2015, 1, 12, 10, 10, 10),
    datetime(2015, 1, 12, 11, 0, 0),
    datetime(2015, 1, 12, 11, 10, 10),
],datetime(2015, 1, 12, 10, 10, 0)))