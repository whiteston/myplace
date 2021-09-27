"""
Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees.

If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

Input : The time of the day.
Output : The angle of the sun, rounded to 2 decimal places.

Example:

sun_angle("07:00") == 15
sun_angle("12:15") == 93.75
sun_angle("01:23") == "I don't see the sun!"

Precondition : 00:00 <= time <= 23:59
"""


from typing import Union


def sun_angle(time: str) -> Union[int, str]: # Union: 매개변수 str로 받지만 여러 개의 타입 입력 허용해줄 때 
    nt = time.split(":")
    if 6 <= int(nt[0]) < 18 and 00 <= int(nt[1]) <= 59 or time == "18:00":
        if int(nt[1]) == 0:
            return (int(nt[0]) - 6) * 15
        return ((int(nt[0]) - 6) * 15) + (float(nt[1]) * 0.25)
    else:
        return "I don't see the sun!"

print(sun_angle("18:01"))
print(sun_angle("14:43"))


# 도움이 되었던 아이디어

#    hours = int(time.split(":")[0])
#    minutes = int(time.split(":")[1])
#
#    Union = (hours * 60 + minutes - 360) / 4
#    # 시간을 분으로 환산해서 
#    return Union if 0 <= Union <= 180 else "I don't see the sun!"
#
#print(sun_angle("17:51"))