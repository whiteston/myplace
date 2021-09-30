"""
# 2주차_상호 평가

대학 교수인 당신은, 상호평가를 통하여 학생들이 제출한 과제물에 학점을 부여하려고 합니다. 
아래는 0번부터 4번까지 번호가 매겨진 5명의 학생들이 자신과 다른 학생의 과제를 평가한 점수표입니다.
당신은 각 학생들이 받은 점수의 평균을 구하여, 기준에 따라 학점을 부여하려고 합니다.

만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.

제외할 점수는 제외하고 평균을 구한 후, 아래 기준에 따라 학점을 부여합니다.
학생들의 점수가 담긴 정수형 2차원 배열 scores가 매개변수로 주어집니다.
이때, 학생들의 학점을 구하여 하나의 문자열로 만들어서 return 하도록 solution 함수를 완성해주세요.

Example:

No.	0	1	2	3	4
0	100	90	98	88	65
1	50	45	99	85	77
2	47	88	95	80	67
3	61	57	100	80	65
4	24	90	94	75	65
평균	45.5	81.25	97.2	81.6	67.8

0번 학생이 받은 점수는 0번 열에 담긴 [100, 50, 47, 61, 24]입니다.
자기 자신을 평가한 100점은 자신이 받은 점수 중에서 유일한 최고점이므로, 평균을 구할 때 제외합니다.
0번 학생의 평균 점수는 (50+47+61+24) / 4 = 45.5입니다.

Precondition:

- 2 ≤ scores의 행의 길이(학생 수) ≤ 10
- scores의 열의 길이 = scores의 행의 길이. 즉, scores는 행과 열의 길이가 같은 2차원 배열입니다.
- 0 ≤ scores의 원소 ≤ 100
- return 값 형식
    :0번 학생의 학점부터 차례대로 이어 붙인 하나의 문자열을 return 합니다.
"""


def solution(scores):
    def check(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    answer = ''
    avg = []	#각 학생의 평균
 	
    for i in range(len(scores)):
        now = []	#현재 학생의 점수를 모두 담아줄 리스트
        my_score = 0	#자신을 평가한 점수
        
        for j in range(len(scores)):
            now.append(scores[j][i])
            if j == i:
                my_score = scores[j][i]
        
        #1 만약 자신을 평가한 점수가 최댓값 또는 최솟값 일 경우 if 실행
        if my_score == max(now) or my_score == min(now):
            #2 my_score와 같은 점수가 2개 이상이면 바로 평균 계산
            if now.count(my_score) > 1:
                avg.append(sum(now)/len(now))
            #3 그렇지 않다면(유일하다면) 받은 점수에서 자기 점수 제거하고 평균 계산
            else:
                avg.append((sum(now) - my_score)/(len(now) - 1))
        #4 자신을 평가한 점수가 최댓값 또는 최솟값이 아니라면 #2와 같다.
        else:
            avg.append(sum(now)/len(now))


    for a in avg:
        answer += check(a)

    return answer

## 다른 사람의 풀이

#1. from collections import Counter 
# + 학점 만드는 함수까지 동일

# answer = ''
 
#2. 판다스에서 배웠던 transpose를 코드로 표현

# for i in range(len(scores)):
#     for j in range(1, i + 1):
#         scores[i][i - j], socres[i - j][i] = socres[i - j][i], scores[i][i - j]

# -> 문제 예시로 간단히 살펴보면 
# i , range(1, i + 1), 변경 과정        (대칭 구조)
# 0     range(1, 1)        x
# 1     range(1, 2)     [1, 0] = [0, 1]
# 2     range(1, 3)     [2, 1] = [1, 2], [2, 0] = [0, 2]    
# 3     range(1, 4)     [3, 2] = [2, 3], [3, 1] = [1, 3], [3, 0] = [0, 3]
# 4     range(1, 5)     ...

#3. 문제 조건 반영
# avg = []
# for i, s in enumerate(scores):
#     if (max(s) == s[i] or min(s) == s[i]) and Counter(s)[s[i]] == 1:
#         avg.append((sum(s) - s[i]/(len(s) - 1))
#     else:
#         avg.append(sum(s)/len(s))
# rank = ''.join(list(map(rank, avg)))
# return rank