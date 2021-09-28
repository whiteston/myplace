"""
# [3187번 양치기 꿍](https://www.acmicpc.net/problem/3187)

## 6.양치기 꿍

양치기 꿍은 맨날 늑대가 나타났다고 마을 사람들을 속였지만 이젠 더이상 마을 사람들이 속지 않는다.
화가 난 꿍은 복수심에 불타 아예 늑대들을 양들이 있는 울타리안에 마구 집어넣어 양들을 잡아먹게 했다.

하지만 양들은 보통 양들이 아니다. 같은 울타리 영역 안의 양들의 숫자가 늑대의 숫자보다 더 많을 경우 늑대가 전부 잡아먹힌다.
물론 그 외의 경우는 양이 전부 잡아먹히겠지만 말이다.

꿍은 워낙 똑똑했기 때문에 이들의 결과는 이미 알고있다.
만약 빈 공간을 '.'(점)으로 나타내고 울타리를 '#', 늑대를 'v', 양을 'k'라고 나타낸다면 여러분은 몇 마리의 양과 늑대가 살아남을지 계산할 수 있겠는가?

단, 울타리로 막히지 않은 영역에는 양과 늑대가 없으며 양과 늑대는 대각선으로 이동할 수 없다.

Input : 입력의 첫 번째 줄에는 각각 영역의 세로와 가로의 길이를 나타내는 두 개의 정수 R, C (3 ≤ R, C ≤ 250)가 주어진다.
        다음 각 R줄에는 C개의 문자가 주어지며 이들은 위에서 설명한 기호들이다.
Output : 살아남게 되는 양과 늑대의 수를 각각 순서대로 출력한다.
"""


import sys
from collections import deque
input = sys.stdin.readline    # 반복문에서 여러줄 입력받을 때 사용. 시간초과 막을 수 있다. 

R, C = map(int, input().split())
farm = []
for _ in range(R):
    farm.append(list(input().rstrip()))    # 문제에서 주어진 울타리, 양, 늑대 입력 받는다.

check = [[0] * C for _ in range(R)]    # 방문처리 하기 위해
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = [0, 0]    # check[0] -> 양, check[1] -> 늑대

def bfs(i, j):
    s = w = 0
    queue = deque()
    if farm[i][j] == 'v':
        w = 1
    if farm[i][j] == 'k':
        s = 1
    queue.append((i,j))
    check[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in steps:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < R) and (0 <= ny < C) and farm[nx][ny] != '#' and not check[nx][ny]:
                check[nx][ny] = 1
                if farm[nx][ny] == 'k':
                    s += 1
                elif farm[nx][ny] == 'v':
                    w += 1
                queue.append((nx, ny))
    if s > w:
        count[0] += s
    else:
        count[1] += w

for i in range(R):
    for j in range(C):
        if farm[i][j] != '#' and not check[i][j]:    # 현재 칸이 #가 아니면 bfs 실행한다.
            bfs(i, j)
            

print(*count)

# *args, **kwargs 에 대한 설명
# https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs