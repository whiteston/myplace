"""
# 3.구름다리를 건너는 토끼

토끼가 구름다리로 강을 건너려고 합니다.

다리를 건너려는데 이런 글귀가 적혀 있네요.

        - 알림 -
구름다리의 각 발판에는 자연수가 적혀있으며,
자신이 밟고 있는 발판에 적혀있는 숫자만큼
앞쪽으로 점프해야 한다.
당신은 반드시 첫 번째 발판에서부터 
구름다리를 건너기 시작해야 한다.
- - - - - - - - - - - - - - - - - - - - - - 
구름다리의 발판에 적혀있는 

숫자가 순서대로 들어있는 리스트 steps가 매개변수로 주어질 때,

구름다리를 끝까지 건너기 위해 

필요한 점프 횟수를 반환하는 cross_bridge 함수 를 작성해 보아요.
"""


def cross_bridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    
    while (current < n):
        
        current = current + steps[current]
        cnt = cnt + 1
    return cnt

print(cross_bridge([1, 1, 2, 3, 5]))