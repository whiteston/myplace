"""
# [15922번 수들의 합](https://www.acmicpc.net/problem/15922)

## 6.아우으 우아으이야!!


수직선 위에 선분을 여러 개 그릴 거 야아!

선분을 겹치게 그리는 것도 가능하다아!!

선분을 모두 그렸을 때, 수직선 위에 그려진 선분 길이의 총합은 얼마아!!!

Input : 첫째 줄에 수직선 위에 그릴 선분의 개수 N이 주어진다!. (1 ≤ N ≤ 100,000)
        둘째 줄 부터 N개의 줄에 좌표를 나타내는 정수쌍 (x, y)가 주어진다.
        이는 [x, y] 구간 (x와 y를 포함하는 구간)에 선분을 그린다는 의미이다아이양. 
        좌표는 x가 증가하는 순으로, x가 같다면 y가 증가하는 순으로 주어진다으. (-1,000,000,000 ≤ x < y ≤ 1,000,000,000)
Output: N개의 선분을 모두 그렸을 때, 수직선 위에 그어진 선분 길이의 총합을 출력한다!
"""


N = int(input())
x, y =map(int, input().split())
result = 0

for _ in range(N - 1):
    nx, ny = map(int, input().split())

    if x <= ny <= y:
        continue
    elif x <= nx <= y and not x <= ny <= y:
        y = ny
    else:
        result += y - x
        x, y = nx, ny

print(result + (y - x))