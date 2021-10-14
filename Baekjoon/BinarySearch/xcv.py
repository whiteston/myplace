import sys
input = sys.stdin.readline

def find(num):
    N, b = 1, len(new_Ai) - 1
    while N < b:
        m = (N + b) // 2
        if new_Ai[m] < num:
            N = m + 1
        elif new_Ai[m] > num:
            b = m
        else:
            N = b = m
    return b

N = int(input())
Ai = list(map(int, input().split()))
new_Ai = [0]

for i in Ai:
    if new_Ai[-1] < i:
        new_Ai.append(i)
    else:
        new_Ai[find(i)] = i

print(len(new_Ai) - 1)

