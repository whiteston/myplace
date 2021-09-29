"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

Input :Date and time as a string
Output :The same date and time, but in a more readable format

Example:

date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# NB: words "hour" and "minute" are to be used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases "hours" and "minutes" should be used.

Precondition :
0 < day <= 31
0 < month <= 12
0 < year <= 3000
0 <= hours < 24
0 <= minutes < 60
"""


month = {
    1 : 'January',
    2 : 'February',
    3 : 'March',
    4 : 'April',
    5 : 'May',
    6 : 'June',
    7 : 'July',
    8 : 'August',
    9 : 'September', 
    10 : 'October',
    11 : 'November',
    12 : 'December'
}


def date_time(time: str) -> str:
    

    left = time.split(' ')[0]
    right = time.split(' ')[1]

    left_num = left.split('.')
    right_num = right.split(':')

    h = 'hour' if right_num[0] == '01' else 'hours'
    m = 'minute' if right_num[1] == '01' else 'minutes'

    return "{} {} {} year {} {} {} {}".format(int(left_num[0]), month[int(left_num[1])], left_num[2],\
        int(right_num[0]), h, int(right_num[1]), m)
    #elif right_num[1] == '01':
    #    return "{} {} {} year {} hours {} minute".format(int(left_num[0]), month[int(left_num[1])], left_num[2],\
    #    int(right_num[0]), int(right_num[1]))
    #elif right_num[0] == '01' or right_num[1] == '01':
    #    return "{} {} {} year {} hour {} minute".format(int(left_num[0]), month[int(left_num[1])], left_num[2],\
    #    int(right_num[0]), int(right_num[1]))
    #
    #return "{} {} {} year {} hours {} minutes".format(int(left_num[0]), month[int(left_num[1])], left_num[2],\
    #    int(right_num[0]), int(right_num[1]))``

print(date_time("19.09.2999 02:01"))

#from datetime import datetime
#def date_time(time: str) -> str:    
#    return (d := datetime.strptime(time, "%d.%m.%Y %H:%M")).strftime(f"{d.day} %B %Y year {d.hour} hour{'s'*(d.hour != 1)} {d.minute} minute{'s'*(d.minute != 1)}")

#from datetime import datetime
#
#def date_time(time: str) -> str:
#    s=lambda x: 's' if x!=1 else ''
#    dt=datetime.strptime(time,'%d.%m.%Y %H:%M')
#    st=dt.strftime('%-d %B %Y year %-H hour' + s(dt.hour)  + ' %-M minute' + s(dt.minute))
#    return st