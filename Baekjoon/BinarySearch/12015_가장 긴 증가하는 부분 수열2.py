"""
# [12015번 가장 긴 증가하는 부분 수열2](https://www.acmicpc.net/problem/7795)


수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

Input : 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
        둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)
Output : 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
"""


import sys
input = sys.stdin.readline

def find(num):
    N, b = 1, len(new_Ai) - 1
    while N < b:
        m = (N + b) // 2
        if new_Ai[m] < num:
            N = m + 1
        elif new_Ai[m] > num:
            b = m
        else:
            N = b = m
    return b

N = int(input())
Ai = list(map(int, input().split()))
new_Ai = [0]

for i in Ai:
    if new_Ai[-1] < i:
        new_Ai.append(i)
    else:
        new_Ai[find(i)] = i

print(len(new_Ai) - 1)

