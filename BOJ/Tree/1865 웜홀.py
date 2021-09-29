import heapq

T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split()) 
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))
    for _ in range(W):
        a, b, w = map(int, input().split())
        graph[a].append((-w, b))

    answer = "NO"

    for start in range(1, N+1):
        count = 0
        times = [float("INF") for _ in range(N+1)]
        heap = []
        heapq.heappush(heap, (0, start))
        while heap:
            cur_time, cur_city = heapq.heappop(heap)
            if cur_time >= times[cur_city]:
                continue
            if cur_city == start and cur_time < 0:
                answer = "YES"
                break
            if count > 10**4:
                break
            times[cur_city] = cur_time
            for edge in graph[cur_city]:
                time, next_city = edge
                heap.append((cur_time + time, next_city))
                count += 1
        if answer == "YES":
            break

    print(answer)

# 벨만 포드 알고리즘을 통해서 더 깔끔한 풀이 가능
