"""
# [2810번 컵홀더](https://www.acmicpc.net/problem/2810)

## 1.컵홀더

극장의 한 줄에는 자리가 N개가 있다. 서로 인접한 좌석 사이에는 컵홀더가 하나씩 있고, 양 끝 좌석에는 컵홀더가 하나씩 더 있다.
또, 이 극장에는 커플석이 있다. 커플석 사이에는 컵홀더가 없다.

극장의 한 줄의 정보가 주어진다. 이때, 이 줄에 사람들이 모두 앉았을 때, 컵홀더에 컵을 꽂을 수 있는 최대 사람의 수를 구하는 프로그램을 작성하시오.
모든 사람은 컵을 한 개만 들고 있고, 자신의 좌석의 양 옆에 있는 컵홀더에만 컵을 꽂을 수 있다.

S는 일반 좌석, L은 커플석을 의미하며, L은 항상 두개씩 쌍으로 주어진다.

어떤 좌석의 배치가 SLLLLSSLL일때, 컵홀더를 *로 표시하면 아래와 같다.

                        -- *S*LL*LL*S*S*LL* --

위의 예에서 적어도 두 명은 컵홀더를 사용할 수 없다.

Input : 첫째 줄에 좌석의 수 N이 주어진다. (1 ≤ N ≤ 50) 둘째 줄에는 좌석의 정보가 주어진다.
Output: 컵을 컵홀더에 놓을 수 있는 최대 사람의 수를 출력한다.
"""


N = int(input()) # 좌석의 수 N이 주어진다. (1 ≤ N ≤ 50)
seat = input() # 좌석 정보를 입력한다.

count = 0
for i in range(len(seat)):  # seat에 들어온 문자를 하나씩 꺼낸다.
    if seat[i] == 'L':
        count += 1 # L을 카운트해서 결과에 반영하는게 포인트인 것 같음.

if count == 0: # N이 주어질 때 커플석이 없다면 최대 사람 수는 (N + 1) 값을 가진다. 그러나 *최대 사람의 수는 N이다. 
    print(N) 
else:
    # (L = 2): 커플석 1세트. -> count // 2
    # 세트가 늘어날 때마다 '최대 사람의 수'가 1명씩 감소
    print(N - (count // 2 - 1))
        

        