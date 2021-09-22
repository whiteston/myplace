"""
# [5576번 콘테스트](https://www.acmicpc.net/problem/5576)

## 1.콘테스트

최근 온라인에서의 프로그래밍 콘테스트가 열렸다. W 대학과 K 대학에서 각각 10 명씩이 콘테스트에 참여했다.
긴 논의 끝에 참가한 10 명 중 득점이 높은 사람에서 3 명의 점수를 합산하여 대학의 득점으로하기로 했다.

W 대학 및 K 대학 참가자의 점수 데이터가 주어진다. 이때, 각각의 대학의 점수를 계산하는 프로그램을 작성하라.

Input : 입력은 20 행으로 구성된다. 1 번째 줄부터 10 번째 줄에는 W 대학의 각 참가자의 점수를 나타내는 정수
        11 번째 줄부터 20 번째 줄에는 K 대학의 각 참가자의 점수를 나타내는 정수가 적혀있다. 정수는 모두 0 이상 100 이하이다.
Output: W 대학 점수와 K 대학의 점수를 순서대로 공백으로 구분하여 출력하라.
"""


W_score = []
K_score = []

for i in range(10):
    W_score.append(int(input()))
for i in range(10, 20):
    K_score.append(int(input()))

W_score = sorted(W_score, reverse=True) 
K_score = sorted(K_score, reverse=True)

print("{} {}".format(sum(W_score[0:3]), sum(K_score[0:3])))
        