"""
# [3541번 상근타워](https://www.acmicpc.net/problem/3541)


상근이는 남는 돈으로 매우 높은 빌딩 "상근타워"를 지었다.
상근타워에는 엘리베이터가 m개가 있다. 각 엘리베이터에는 두 버튼이 있다. i번째 엘리베이터의 한 버튼은 ui 층을 올라가는 버튼이고, 다른 버튼은 di층 내려가는 버튼이다.

상근타워의 가장 아래층(로비)은 0층이고, 그 다음 층부터는 증가하는 자연수이다.
엘리베이터를 타고 지하로 내려갈 수 없으며, 건물은 매우 높아 끝이 없다고 가정한다.

상근이는 상근타워의 로비에 서있다. 이제, 엘리베이터중 하나를 골라서 타려고 한다. 엘리베이터를 탄 이후에는 다른 엘리베이터로 바꿔탈 수 없다.
이때, 엘리베이터 버튼을 정확하게 n번 눌러서 갈 수 있는 가장 낮은 층(로비는 제외)을 구하는 프로그램을 작성하시오.

Input : 첫째 줄에 n과 m이 주어진다. (1 ≤ n ≤ 1,000,000, 1 ≤ m ≤ 2,000) 다음 m개 줄에는 각 엘리베이터의 버튼 ui와 di가 주어진다. (1 ≤ ui, di ≤ 1000)
Output : 엘리베이터를 타고 버튼을 n번 눌러서 갈 수 있는 가장 낮은 층을 출력한다.
"""


import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

button = []
for _ in range(m):
    button.append(list(map(int, input().split())))

def search(start, left, right):
    count = 1
    while count < n:
        if left >= right:
            left = left - right
            count += 1
        else:
            left = left + start
            count += 1
    return left

array = []
for i in button:
    array.append(search(i[0], i[0], i[1]))

print(min(array))