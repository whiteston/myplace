"""
# 4.토끼와 거북이의 달리기 경주

토끼와 거북이가 달리기 경주를 시작했습니다.

토끼는 N분에 한번 휴식을 하고 거북이는 M분에 한번 휴식을 한다고 합니다.

토끼와 거북이가 처음으로 같은 타이밍에 쉬는 시간은 언제일까요?
"""


a, b = [int(i) for i in input().split()]

def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

def lcm(a, b):
    gcd_value = gcd(a, b)
    return a * b / gcd_value

# N과 M의 최소공배수를 구하기 위해서는 N과 M의 곱을 최대공약수로 나누어주면 된다.
# 최대공약수를 구하기 위한 방법 중 유클리드 호제법을 적용
# -> 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다.