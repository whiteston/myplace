"""
# [2579번 계단 오르기](https://www.acmicpc.net/problem/2579)

## 16.계단 오르기

계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 
하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

Input : 입력의 첫째 줄에 계단의 개수가 주어진다.
        둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 
        계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.
Output : 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.
"""


import sys
input = sys.stdin.readline

k = int(input())
stair = [0]

for i in range(k):
    stair.append(int(input()))

select = [0]
    # 처음 3개 계단 값을 활용해 select 구성.
for i in range(1, k + 1):
    if i == 1:
        select.append(stair[i])
    elif i == 2:
        select.append(stair[i] + stair[i - 1])
    
    # 그 이후로는 규칙에 따라 이런 관계를 가진다.
    else:
        select.append(max(select[i - 3] + stair[i - 1] + stair[i], select[i - 2] + stair[i]))
     
print(select[k])