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


c, r = map(int, input().split())
cheese = [list(map(int, input().split().strip())) for _ in range(c)]

def test(cheese, c, r):
    for i in range(c):
        for j in range(r):
            if cheese[i][j] == 1:
                return True
    return False

print(test
# column = int(input_cheese[0])
# row = int(input_cheese[1])

# for i in range(column):
#     for j in range(row):
#         print(i, j) 
