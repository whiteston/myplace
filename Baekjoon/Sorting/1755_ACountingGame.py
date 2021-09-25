"""
# [1755번 숫자놀이](https://www.acmicpc.net/problem/1755)

## 6.숫자놀이

79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 
79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M, N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 
숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.


Input : 첫째 줄에 M과 N이 주어진다.
Output: M 이상 N 이하의 정수를 문제 조건에 맞게 정렬하여 한 줄에 10개씩 출력한다.
"""


m, n = map(int, input().split())

alphabet = {'0' : 'zero',
            '1' : 'one',
            '2' : 'two',
            '3' : 'three',
            '4' : 'four',
            '5' : 'five',
            '6' : 'six',
            '7' : 'seven',
            '8' : 'eight',
            '9' : 'nine'
 }

mn = []

for num in range(m, n + 1):
    k = ''.join([alphabet[c] for c in str(num)]) # 처음에 숫자와 영어단어를 따로 만들었다.
                                                 # 그러면 식이 복잡해진다. 그래서 함께 생각하기로 했다.
    mn.append([num, k])

mn.sort(key = lambda x: x[1])                    # lambda 사용해서 x[1] 값 즉, 영어단어 기준으로 정렬한다.
for num in range(len(mn)):
#    print(mn)
    if num % 10 == 0 and num != 0:
        print()
    print(mn[num][0], end=" ")                  # 40번 줄에서 print 해보면 알겠지만 mn은 리스트가 중첩되어 있다.
                                                # 그래서 mn에서 반복문 돌려서 각 리스트에 접근한 다음 첫 번째 인덱스를 출력한다.


     