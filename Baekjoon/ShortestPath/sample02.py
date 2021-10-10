# 2.개선된 데이크스트라 알고리즘
  ## 힙(Heap) 자료구조를 사용 -> 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아서 처리
                                #출발 노드로부터 가장 거리가 짧은 노드를 더욱 빠르게 찾을 수 있다.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10억 = 무한을 의미하는 값

n, m = map(int, input().split())
start = int(input())
# start에 설정한 노드까지 오는 거리를 포함 -> range(n + 1)
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 어느 큐에 삽입할지, 시작 노드로 가기 위한 최단 경로는 0으로 설정
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
