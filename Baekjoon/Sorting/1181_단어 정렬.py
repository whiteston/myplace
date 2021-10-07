"""
# [1181번 단어 정렬](https://www.acmicpc.net/problem/1181)

## 19.단어 정렬

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1.길이가 짧은 것부터
2.길이가 같으면 사전 순으로

Input : 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.
Output : 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
"""


import sys

N = int(sys.stdin.readline())
m = [sys.stdin.readline().rstrip() for _ in range(N)]
set_m = set(m)
k = list(set_m)

k.sort()
k.sort(key = len)

# for 반복문 2번 사용해서 하나씩 비교하고 정렬하는 방법으로 풀었는데 시간초과

#for i in range(1, len(k)):
#    for j in range(i, 0, -1):
#        if len(k[j]) < len(k[j - 1]):
#            k[j], k[j - 1] = k[j - 1], k[j]
#        else:
#            break

print('\n'.join(k))
