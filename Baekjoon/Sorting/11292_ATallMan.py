"""
# [11292번 키 큰 사람](https://www.acmicpc.net/problem/11292)

## 8.키 큰 사람

민우는 학창시절 승부욕이 강해서 달리기를 할 때에도 누가 가장 빠른지를 중요하게 생각하고, 
시험을 볼 때에도 누가 가장 성적이 높은지를 중요하게 생각한다. 
이번에 반에서 키를 측정하였는데, 민우는 마찬가지로 누구의 키가 가장 큰지 궁금해한다. 민우를 도와 가장 키가 큰 사람을 찾아보자.

Input : 입력은 여러개의 테스트케이스로 구성되어있다. 
        각 테스트케이스는 첫 번째 줄에 학생의 수 N (0 < N ≤ 50)이 주어지고, 이어서 N개의 줄에 각 학생의 이름과 키가 공백으로 구별되어 주어진다.
        학생의 이름은 알파벳 대/소문자로만 이루어져 있고, 길이는 10을 넘지 않는다. 
        학생의 키는 소숫점 이하 2자리까지 주어진다. N이 0으로 주어지는 경우 프로그램을 종료한다.
Output : 각 테스트케이스에 대해, 가장 키가 큰 학생의 이름을 한 줄에 출력한다. 
         같은 키의 사람이 여러명 일 경우 모두 출력해야 하며, 순서는 입력으로 들어온 순서를 유지해야 한다.
"""


while True:
    N = int(input())    # 학생의 수 N을 입력한다.

    if N == 0:    # N이 0으로 주어지면 프로그램을 종료한다.
        break
    else:    # N이 0이 아니라면 학생들의 이름과 키의 정보를 저장하는 리스트를 선언한다.
        students = []
        for _ in range(N):
            student = input().split(' ')

            student[1] = float(student[1])    # 키는 실수형으로 변환
            students.append(student)    # 입력 받은 값 students 리스트에 추가

        # max_height = max(students, key = lambda student: student[1])[0]    
        # 키를 기준으로 최대값을 가지는 사람의 이름을 출력.
        
        # 여기서 끝내면 같은 키를 가진 사람이 여러 명일 경우 가장 앞에 있는 사람만 출력하는 문제 발생.
        
        max_height = max(students, key = lambda student: student[1])[1]
        # max_height를 '이름'이 아닌 '키'로 변경한 다음 
        
        for student in students:    # 반복문을 돌려서 max_height와 같으면 모두 출력하는 식 추가.
            if student[1] == max_height:
                print(student[0], end = ' ')
        print()
