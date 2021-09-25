"""
# [16212번 정열적인 정렬](https://www.acmicpc.net/problem/16212)

## 4.정열적인 정렬

형준이는 수열을 하나 가지고 있다. 형준이는 수열을 정열적으로 정렬해보려 한다. 과연, 정렬할 수 있을까?


Input : 첫째 줄에는 수열의 길이 N (1 ≤ N ≤ 500,000)이 주어진다.
        둘째 줄에는 수열의 각 원소 ai가 공백을 사이에 두고 차례대로 주어진다. ai의 절댓값은 200만 이하이다.
Output: 수열 a를 오름차순으로 정렬해서, 공백을 사이에 두고 하나씩 차곡차곡 출력하자.
"""


N = int(input())
ai = list(map(int, input().split()))

print(' '.join(list(map(str, sorted(ai)))))
