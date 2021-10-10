# 플로이드 워셜 알고리즘 -> 2차원 리스트에 '최단 거리' 정보를 저장한다는 특징
# 매번 방문하지 않은 노드 중에서 최단 거리를 갖는 노드를 찾을 필요가 없다.
# 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행. '현재 노드를 거쳐 가는' 모든 경로를 고려

INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트 만들고, 모든 값을 무한으로
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 설명에 나와있듯이 자기 자신으로 가는 비용은 0으로 설정.
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식으로 표현하는 이 과정이 포인트
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end=" ")
        else:
            print(graph[a][b], end= " ")
    print()