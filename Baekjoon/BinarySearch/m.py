import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

button = []
for _ in range(m):
    button.append(list(map(int, input().split())))

def search(start, left, right):
    count = 1
    while count < n:
        if left >= right:
            left = left - right
            count += 1
        else:
            left = left + start
            count += 1
    return left

array = []
for i in button:
    array.append(search(i[0], i[0], i[1]))

print(min(array))