import heapq

def minimum_fare(start, graph):
    INF = float('inf')
    distance = [INF for _ in range(len(graph))]
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, cur = heapq.heappop(heap)
        if distance[cur] < dist:
            continue
        for edge in graph[cur]:
            cost = dist + edge[0]
            next_node = edge[1]
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))
    return distance


def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        node1, node2, w = map(int, fare)
        graph[node1].append((w, node2))
        graph[node2].append((w, node1))
    fare_to_a = minimum_fare(a, graph)
    fare_to_b = minimum_fare(b, graph)
    fare_from_start = minimum_fare(s, graph)
    total_fare = [fare_from_start[i]+fare_to_a[i]+fare_to_b[i] for i in range(1,n+1)]
    answer = min(total_fare)

    return answer
