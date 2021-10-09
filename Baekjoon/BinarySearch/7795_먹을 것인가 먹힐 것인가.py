"""
# [7795번 먹을 것인가 먹힐 것인가](https://www.acmicpc.net/problem/7795)


심해에는 두 종류의 생명체 A와 B가 존재한다. A는 B를 먹는다. A는 자기보다 크기가 작은 먹이만 먹을 수 있다.
예를 들어, A의 크기가 {8, 1, 7, 3, 1}이고, B의 크기가 {3, 6, 1}인 경우에 A가 B를 먹을 수 있는 쌍의 개수는 7가지가 있다. 8-3, 8-6, 8-1, 7-3, 7-6, 7-1, 3-1.

두 생명체 A와 B의 크기가 주어졌을 때, A의 크기가 B보다 큰 쌍이 몇 개나 있는지 구하는 프로그램을 작성하시오.

Input : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 A의 수 N과 B의 수 M이 주어진다. 둘째 줄에는 A의 크기가 모두 주어지며, 셋째 줄에는 B의 크기가 모두 주어진다. 크기는 양의 정수이다. (1 ≤ N, M ≤ 20,000) 
Output : 각 테스트 케이스마다, A가 B보다 큰 쌍의 개수를 출력한다.
"""


import sys
input = sys.stdin.readline
# 조금 더 연습해보면서 이분탐색 식에 익숙해져야 할 거 같다.
def search(target, data):
    start = 0
    end = len(data) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

# 입력 받는 건 이제 어렵지 않게 작성할 수 있다.
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    array_a = list(map(int, input().split()))
    array_b = list(map(int, input().split()))
    
    count = 0
    array_a.sort()
    array_b.sort()
    
    for i in array_a:
        count += search(i, array_b) + 1
    
    print(count)