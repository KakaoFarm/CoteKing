import sys
import heapq

sys.setrecursionlimit(10*5)

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    node1, *edges, end = map(int, input().split())
    for i in range(len(edges)//2):
        node2 = edges[2*i]
        dist = edges[2*i+1]
        graph[node1].append((dist, node2))

answer = 0
is_visited = [False]*(V+1)

def get_max_child(node):
    global answer
    is_visited[node] = True
    children = graph[node]
    dists = []
    for dist, child in children:
        if not is_visited[child]:
            value = get_max_child(child) + dist
            heapq.heappush(dists, (-value, value))
    if not dists:
        return 0
    largest_dist = heapq.heappop(dists)[1]
    second_largest_dist = 0
    if dists:
        second_largest_dist = heapq.heappop(dists)[1]
    answer = max(answer, largest_dist + second_largest_dist)
    return largest_dist

get_max_child(1)
print(answer)
