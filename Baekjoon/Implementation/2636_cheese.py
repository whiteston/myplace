"""
# [2636번 치즈](https://www.acmicpc.net/problem/2636)

## 2.치즈

정사각형 칸들로 이루어진 사각형 모양의 판이 있고, 그 위에 얇은 치즈가 놓여 있다.
판의 가장자리에는 치즈가 놓여 있지 않으며 치즈에는 하나 이상의 구멍이 있을 수 있다.

이 치즈를 공기 중에 놓으면 녹게 되는데 공기와 접촉된 칸은 한 시간이 지나면 녹아 없어진다.
치즈의 구멍 속에는 공기가 없지만 구멍을 둘러싼 치즈가 녹아서 구멍이 열리면 구멍 속으로 공기가 들어가게 된다.

-치즈의 구멍을 둘러싼 치즈는 녹지 않고 ‘c’로 표시된 부분만 한 시간 후에 녹아 없어진다.

입력으로 사각형 모양의 판의 크기와 한 조각의 치즈가 판 위에 주어졌을 때,

치즈가 모두 녹아 없어지는 데 '걸리는 시간'과 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 '칸의 개수'를 구하는 프로그램을 작성하시오.

Input: 첫째 줄에는 사각형 모양 판의 세로와 가로의 길이가 양의 정수로 주어진다.
       세로와 가로의 길이는 최대 100이다. 판의 각 가로줄의 모양이 윗 줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다.
       치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.
Output: 첫째 줄에는 치즈가 모두 녹아서 없어지는 데 걸리는 시간을 출력하고,
        둘째 줄에는 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수를 출력한다.
"""

import collections

c, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(c)]

dx = [-1, 1, 0, 0] #상/하 이동
dy = [0, 0, -1, 1] #좌/우 이동

def bfs():
    queue = collections.deque()
    queue.append((0,0))
    check = [[False] * r for _ in range(c)]

    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if board[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append((nx,ny))
                # (0,0)에서 시작해서 처음 만나는 1들은 모두 가장자리이다.
                elif board[nx][ny] == 1:
                    # 1을 만나면 0으로 바꿔줘 녹게 만들어준다.
                    board[nx][ny] = 0
                    count += 1
                    check[nx][ny] = True
    return count

result = []
time = 0
while True:
    count = bfs()
    result.append(count)
    # count가 0이면 모든 치즈가 녹았다는 소리이다.
    if count == 0:
        break
    time += 1

print(time)
# 한시간 전에(모두 녹기전 단계) count를 출력해야 되므로 [-2]를 출력한다.
print(result[-2])