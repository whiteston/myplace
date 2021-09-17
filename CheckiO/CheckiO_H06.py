'''
How old are you in a number of days? 
We could make this a real challenge though and count the difference between any dates.

You are given two dates as an array with three numbers - a year, month and day.
For example: 19 April 1982 will be (1982, 4, 19).
You should find the difference in days between the given dates.
For example between today and tomorrow = 1 day.
The difference will always be either a positive number or zero, so don't forget about the absolute value.

Input: Two dates as tuples of integers.
Output: The difference between the dates in days as an integer.

Example:

days_diff((1982, 4, 19), (1982, 4, 22)) == 3
days_diff((2014, 1, 1), (2014, 8, 27)) == 238

Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.
'''


from datetime import datetime

def days_diff(a, b):
    a = datetime(year=a[0], month=a[1], day=a[2])
    b = datetime(year=b[0], month=b[1], day=b[2])
    return abs((a - b).days)

# datetime 함수에 대한 이해가 부족한 듯.
# 튜플로 받은 날짜를 strptime(), int() 등 다양한 함수를 사용해봤으나 Error 발생
# a, b에 입력 받은 날짜 형식을 연,월,일로 구분해서 datetime에 넣어준다.
# 아래의 식처럼 튜플 기능을 활용해 한 줄로 표현 가능.
    # return (abs((datetime(a[0],a[1],a[2]))-(datetime(b[0],b[1],b[2]))).days)

print(days_diff((1996, 5, 7), (1998, 9, 10)))