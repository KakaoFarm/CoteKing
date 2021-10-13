import heapq

N = int(input())
M = int(input())
graph = [dict() for _ in range(N+1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], w)
    else:
        graph[a][b] = w

def solution(graph, start):
    dist = [float('INF') for _ in range(N+1)]
    heap = [(0, start)]
    while heap:
        X, node = heapq.heappop(heap)
        if X > dist[node]:
            continue
        dist[node] = X
        for link in graph[node].keys():
            next_dist, next_node = graph[node][link], link
            heapq.heappush(heap, (X + next_dist, next_node))
    for i in range(len(dist)):
        if dist[i] == float('INF'):
            dist[i] = 0
    return dist[1:]

for i in range(1,N+1):
    print(*solution(graph, i))
