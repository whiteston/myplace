import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
# start에 설정한 노드까지 오는 거리를 포함 -> range(n + 1)
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미

    graph[a].append((b, c))

# 1.간단한 데이크스트라 알고리즘
  ## 시간 복잡도 : O(V^2), O(V)번에 걸쳐서 '최단 거리가 가장 짧은 노드'를 매번 선형 탐색.
                   # 현재 노드와 연결된 노드를 매번 일일이 확인하기 때문.
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        # 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드 번호 반환
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해서 초기화
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1): # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
        now = get_smallest_node() #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]: # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

# 2.개선된 데이크스트라 알고리즘
  ## 힙(Heap) 자료구조를 사용 -> 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리
                                #출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

