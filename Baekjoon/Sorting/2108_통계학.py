"""
# [2108번 통계학](https://www.acmicpc.net/problem/2108)

## 21.통계학

수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

-산술평균 : N개의 수들의 합을 N으로 나눈 값
-중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
-최빈값 : N개의 수들 중 가장 많이 나타나는 값
-범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

Input : 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
Output :첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
        둘째 줄에는 중앙값을 출력한다.
        셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
        넷째 줄에는 범위를 출력한다.
"""

import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())

m = []
for _ in range(N):
    m.append(int(sys.stdin.readline()))
m.sort()

# 산술평균
a = round(sum(m) / N)
# 중앙값
b = m[N // 2]

# 최빈값
dict = {}
for i in m:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

m_num = 0
array = []
for key, val in dict.items():
    if val > m_num:
        array.clear()
        array.append(key)
        m_num = val
    elif val == m_num:
        array.append(key)
        m_num = val
array.sort()

# 최빈값이 여러 개 있을 경우, 두 번째로 작은 값 출력
if len(array) == 1:
    c = array[0]
else:
    c = array[1]

# 범위
d = max(m) - min(m)

print("{}\n{}\n{}\n{}".format(a, b, c, d))