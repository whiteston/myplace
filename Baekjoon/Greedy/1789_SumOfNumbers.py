"""
# [1789번 수들의 합](https://www.acmicpc.net/problem/1789)

## 3.수들의 합

서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

Input : 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.
Output: 첫째 줄에 자연수 N의 최댓값을 출력한다.
"""


S = int(input())

N = 1   
sum_data = 0


while True:
    sum_data += N #1 1부터 더하기 시작한다.
    if  sum_data > S: #3 과정을 반복하다가 합이 S보다 커지면 N - 1을 출력한다. (N까지 더했을 때 S를 초과하는 값을 가졌기 때문)
        print(N - 1)
        break
    elif sum_data == S: #4 S와 값이 같다면 N을 바로 출력한다.
        print(N)
        break # 빠져나가는 함수를 안 만들어주면 무한대로 뻗어나간다.
    N += 1 #2 if와 elif 만족하지 않으면 N에 1을 더한다.